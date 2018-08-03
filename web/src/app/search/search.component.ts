import {Component, ElementRef, OnInit, ViewChild} from '@angular/core';
import {WebsocketService} from '../websocket.service';

@Component({
    selector: 'app-search',
    templateUrl: './search.component.html',
    styleUrls: ['./search.component.css'],
    providers: [WebsocketService],
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
            this.input = `Search for a song you ${this.placeholders[Math.floor(Math.random() * this.placeholders.length)]}`;
        }
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
}
