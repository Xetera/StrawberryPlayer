import {Component, OnInit} from '@angular/core';
import {WebsocketService} from '../websocket.service';
import {IncompleteSong, Packet} from '../interfaces';
import {Observable, Observer, Subscriber} from 'rxjs';

@Component({
    selector: 'app-playlist',
    templateUrl: './playlist.component.html',
    styleUrls: ['./playlist.component.scss']
})
export class PlaylistComponent implements OnInit {

    public playlist: IncompleteSong[] = [];
    public observ: Observable<Packet>;
    constructor(public socket: WebsocketService) {
    }

    public createIncompleteSong = (name: string) => {
        return <IncompleteSong> {searchedName: name};
    }

    private setupObservers = () => {
        this.socket.outgoing$.subscribe(item => {
            if (item.event === 'download') {
                this.playlist.push(this.createIncompleteSong(item.body));
            }
        });
    }


    ngOnInit() {
        console.log('setting up observers');
        this.setupObservers();
    }

}
