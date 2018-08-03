import {Component} from '@angular/core';
import {WebsocketService} from './websocket.service';

@Component({
    selector: 'app-root',
    templateUrl: './app.component.html',
    styleUrls: ['./app.component.css'],
    providers: [WebsocketService]
})
export class AppComponent {
    title = 'strawberry-player-web';
    constructor(private client: WebsocketService) {
        console.log('emitting something')
        client.emitSearch('Paralyzer Finger Eleven');
    }
}
