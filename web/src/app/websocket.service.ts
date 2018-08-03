import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import Hashids from 'hashids';
import websocketConnect, {Connection, IWebSocket} from 'rxjs-websockets';
import {QueueingSubject} from 'queueing-subject';
import {Observable} from 'rxjs';
import {shallowEqualArrays} from '@angular/router/src/utils/collection';

@Injectable({
    providedIn: 'root'
})
export class WebsocketService {
    private hasher: Hashids;
    public user: string;
    public queue: QueueingSubject<string>;
    public receiver: Observable<string>;
    public connStatus: Observable<number>;
    constructor(public http: HttpClient) {
        this.hasher = new Hashids('strawberry-player');
        this.user = this.hasher.encode(Date.now());
        this.queue = new QueueingSubject<string>();
        ({messages: this.receiver, connectionStatus: this.connStatus} = websocketConnect('ws://localhost:10000', this.queue));
        this.registerHandlers();
    }

    private createPacket = (event: string, body: string): Packet => ({event, body, user: this.user});

    private dispatch = (event: string, body: string): void => {
        const packet = this.createPacket(event, body);
        const serialized = JSON.stringify(packet);
        this.queue.next(serialized);
    }

    private registerHandlers = () => {
        this.receiver.subscribe(message => console.log(message));
    }

    private handleEvent(packet: MessageEvent) {
    }

    public emitSearch = (search: string) => this.dispatch('download', search);



}
