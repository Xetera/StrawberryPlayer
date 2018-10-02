import {Component, OnInit} from '@angular/core';
import {WebsocketService} from '../websocket.service';

@Component({
    selector: 'app-player',
    templateUrl: './player.component.html',
    styleUrls: ['./player.component.scss']
})
export class PlayerComponent implements OnInit {
    public playing = false;
    constructor(public sock: WebsocketService) {
    }

    ngOnInit() {

    }

    togglePlay() {
        this.playing = !this.playing;
        const pack = this.sock.dispatch('play', '[]');
    }

    get playButtonSrc() {
        return this.playing ? 'assets/pause2.png' : 'assets/play.png';
    }
}
