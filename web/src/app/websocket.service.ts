import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import Hashids from 'hashids';
import {Observable, ReplaySubject, Subject} from 'rxjs';
import {Packet} from './interfaces';

@Injectable({
    providedIn: 'root'
})
export class WebsocketService {
    private hasher: Hashids;
    public user: string;
    public outgoing$: ReplaySubject<Packet>;
    public sock: WebSocket;
    public incoming$: ReplaySubject<Packet>;
    public receiver: Observable<string>;
    public connected = false;
    public connection: Subject<boolean> = new Subject<boolean>();

    constructor(public http: HttpClient) {
        this.hasher = new Hashids('strawberry-player');
        this.outgoing$ = new ReplaySubject<Packet>();
        this.incoming$ = new ReplaySubject<Packet>();
        this.user = this.hasher.encode(Date.now());
        // ({messages: this.receiver, connectionStatus: this.connStatus} = websocketConnect('ws://localhost:10000', this.queue));
        this.registerHandlers();
        this.registerListeners();
    }

    private createPacket = (event: string, payload: string | Object): Packet => {
        let body;
        if (typeof body !== 'string') {
            body = JSON.stringify(payload);
        } else {
            body = payload;
        }
        return {
            event, body, user: this.user
        };
    }

    public dispatch = (event: string, body: Object | string): Packet => {
        const packet = this.createPacket(event, body);
        this.outgoing$.next(packet);
        return packet;
    }

    private registerHandlers = () => {
        this.outgoing$.subscribe(packet => {
            const serialized = JSON.stringify(packet);
            this.sock.send(serialized);
        });
        this.incoming$.subscribe(packet => {
            this.handleEvent(packet);
        });
    }

    private registerListeners = () => {
        this.sock = new WebSocket('ws://localhost:10000');
        this.sock.onmessage = event => {
            const packet: Packet = JSON.parse(event.data);
            this.incoming$.next(packet);
        };
        this.sock.onopen = () => {
            this.connected = true;
            this.connection.next(true);
        };
        this.sock.onclose = () => {
            this.connected = false;
            setTimeout(() => this.registerListeners(), 4000);
            this.connection.next(false);
        };
    };

    public subscribeOutgoing = () => {
        return this.outgoing$.asObservable();
    };

    private handleEvent(packet: Packet) {
    }

    public generateId = () => '_' + Math.random().toString(36).substr(2, 9);
}
