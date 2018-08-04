import { Component, OnInit } from '@angular/core';
import {WebsocketService} from '../websocket.service';

@Component({
  selector: 'app-status',
  templateUrl: './status.component.html',
  styleUrls: ['./status.component.scss']
})
export class StatusComponent implements OnInit {

  constructor(public socket: WebsocketService) { }

  ngOnInit() {
  }

  public getStatus() {
      switch (this.socket.sock.readyState) {
          case 0:
              return '...';
          case 1:
              return 'Running!';
          case 2:
              return 'Connecting closing...';
          case 3:
              return 'Connection closed!';
      }
  }

}
