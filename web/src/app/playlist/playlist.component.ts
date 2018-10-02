import {Component, OnInit} from '@angular/core';
import {WebsocketService} from '../websocket.service';
import {Packet, Song} from '../interfaces';
import {Observable, Observer, Subscriber} from 'rxjs';

@Component({
    selector: 'app-playlist',
    templateUrl: './playlist.component.html',
    styleUrls: ['./playlist.component.scss']
})
export class PlaylistComponent implements OnInit {

    public playlist: { [id: string]: Song } = {};
    public observ: Observable<Packet>;

    constructor(public socket: WebsocketService) {
    }

    public createIncompleteSong = (name: string) => {
        return <Song> {searchedName: name};
    };

    private setupObservers = () => {
        this.socket.outgoing$.subscribe(item => {
            const body = JSON.parse(item.body);
            if (['download', 'search'].includes(item.event)) {
                this.playlist[body['id']] = this.createIncompleteSong(body['song']);
            }
        });
        this.socket.incoming$.subscribe(item => {
            console.log('received a new event');
            const body = JSON.parse(item.body);
            if (item.event === 'search') {
                console.log(this.playlist);
                const existing = this.playlist[body['id']];
                console.log(body)
                const data = body.metadata;
                const obj = {
                    searchedName: existing.searchedName,
                    thumbnail: data.thumbnail,
                    title: data.title,
                    description: data.description,
                    duration: data.duration
                };
                this.playlist[body['id']] = obj;
            }
        });
    };

    public get songs() {
        return Object.values(this.playlist).reverse();
    }

    ngOnInit() {
        console.log('setting up observers');
        this.setupObservers();
    }

}
