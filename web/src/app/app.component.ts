import {Component, OnDestroy, OnInit} from '@angular/core';
import {WebsocketService} from './websocket.service';

@Component({
    selector: 'app-root',
    templateUrl: './app.component.html',
    styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {
    constructor(public socket: WebsocketService) { }
    ngOnInit() { }
}
