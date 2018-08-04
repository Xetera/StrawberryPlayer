import {Component, ElementRef, OnInit, ViewChild} from '@angular/core';
import {WebsocketService} from '../websocket.service';

@Component({
    selector: 'app-search',
    templateUrl: './search.component.html',
    styleUrls: ['./search.component.scss'],
})
export class SearchComponent implements OnInit {
    private placeholders: string[] = [
        'adore', 'love', 'like', 'can\'t get enough of', 'would die without'
    ];
    public input: string;
    public isPlaceholder = true;
    constructor(public socket: WebsocketService) {
        this.checkPlaceholder();
    }

    public checkPlaceholder = () => {
        if (!this.input) {
            this.isPlaceholder = true;
        }
        this.input = this.getRandomPlaceholder();
    }
    public getRandomPlaceholder = () => {
        return `Search for a song you ${this.placeholders[Math.floor(Math.random() * this.placeholders.length)]}`;
    }

    public clearText() {
        this.isPlaceholder = false;
        this.input = '';
    }

    ngOnInit() {
    }

    public onKeydown = (event: KeyboardEvent) => {
        if (event.key === 'Enter') {
            this.socket.search(this.input);
        }
    }
    private handleConnection = () => {
        this.socket.connection.subscribe(online => {
            if (online) {
                this.input = this.getRandomPlaceholder();
            } else {
                this.input = 'Server Unreachable!';
            }
        });
    }

    public fetchStatus = () => {
        if (this.socket.sock.readyState !== 1) {
            return ['unavailable-service', 'placeholder-text', 'warning-box'];
        } else if (this.isPlaceholder) {
            return 'placeholder-text';
        }
    }
}
