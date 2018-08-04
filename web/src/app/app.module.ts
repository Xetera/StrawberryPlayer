import {BrowserModule} from '@angular/platform-browser';
import {NgModule} from '@angular/core';

import {AppComponent} from './app.component';
import {HttpClientModule} from '@angular/common/http';
import {WebsocketService} from './websocket.service';
import { SearchComponent } from './search/search.component';
import {FormsModule} from '@angular/forms';
import { PlaylistComponent } from './playlist/playlist.component';
import { PlayerComponent } from './player/player.component';
import { StatusComponent } from './status/status.component';
import { OverlayComponent } from './overlay/overlay.component';

@NgModule({
    declarations: [
        AppComponent,
        SearchComponent,
        PlaylistComponent,
        PlayerComponent,
        StatusComponent,
        OverlayComponent
    ],
    imports: [
        BrowserModule,
        HttpClientModule,
        FormsModule
    ],
    providers: [WebsocketService],
    bootstrap: [AppComponent]
})
export class AppModule {
}
