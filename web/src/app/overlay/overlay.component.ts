import {Component, OnDestroy, OnInit} from '@angular/core';
import {WebsocketService} from '../websocket.service';

import * as PIXI from 'pixi.js/dist/pixi.js';
import Timer = NodeJS.Timer;

@Component({
    selector: 'app-overlay',
    templateUrl: './overlay.component.html',
    styleUrls: ['./overlay.component.scss']
})
export class OverlayComponent implements OnInit, OnDestroy {
    public render: PIXI.Application;
    private elements: PIXI.Container;
    private timer?: Timer;
    private smallTexts: string[] = [
        'Are we even live?',
        'Kinda getting lonely in here...',
        'Did you forget about me?',
        'Hello? This is client speaking.',
        'It\'s actually considered rude to keep a strawberry waiting.',
        'You didn\'t even check, did you?',
        'You do realize this whole thing doesn\'t work if you don\'t turn on the server... right?'
    ];
    ngOnInit() {
    }


    constructor(public socket: WebsocketService) {
        this.socket.connection.subscribe(async online => {
            console.log(online);
            if (this.timer) {
                clearInterval(this.timer);
            }
            if (online) {
                this.fadeElements(0);
            } else if (!online) {
                if (!this.render) {
                    this.renderImage();
                }
                this.fadeElements(1);
            }
        });
        if (socket.connected) {
            return;
        }
        this.renderImage();
        this.fadeElements(1);
    }

    private fadeElements = (amount) => {
        const current = this.elements.getChildAt(0).alpha;
        const diff = amount - current;
        this.timer = setInterval(() => {
            for (const child of this.elements.children) {
                child.alpha += diff / 10;
                if (child.alpha < 0) {
                    child.alpha = 0;
                } else if (child.alpha > 1) {
                    child.alpha = 1;
                }
            }
            const everyChildReady = this.elements.children.every(child => child.alpha === amount);
            if (everyChildReady) {
                clearInterval(this.timer);
                if (!amount) {
                    this.render.destroy(true);
                    this.render = null;
                }
                return;
            }
        }, 50);
    };

    public ngOnDestroy() {
        console.log('REMOVED');
        document.body.removeChild(this.render.view);
    }

    public renderImage() {
        this.render = new PIXI.Application(window.innerWidth, window.innerHeight,
            {transparent: true});
        this.render.view.style.position = 'fixed';
        this.render.view.style.top = '0';
        document.body.appendChild(this.render.view);
        this.elements = new PIXI.Container();
        const background = new PIXI.Graphics();

        background.beginFill(0x1099bb);
        background.drawRect(0, 0, this.render.screen.width, this.render.screen.height);
        const strawberry = PIXI.Sprite.from('assets/strawberry_stroke.png');
        strawberry.anchor.set(0.55);
        const style = new PIXI.TextStyle({
            fill: '#fcfff2',
            fontFamily: '"Trebuchet MS", Helvetica, sans-serif',
            fontSize: 72,
            fontVariant: 'small-caps',
            fontWeight: 'bolder',
            stroke: '#ffffff',
            strokeThickness: 3
        });
        const label = 'Connecting to the server';
        const text: PIXI.Text = new PIXI.Text(label, style);
        strawberry.scale = new PIXI.Point(0.5, 0.5);
        strawberry.name = 'strawberry';
        strawberry.x = this.render.screen.width / 2;
        strawberry.y = 0;
        text.x = strawberry.x - text.width / 2;
        text.y = this.render.screen.height;
        // fading it in
        background.alpha = 0.1;
        this.elements.addChild(background);
        text.alpha = 0.1;
        text.name = 'text';
        this.elements.addChild(text);
        strawberry.alpha = 0.1;
        this.elements.addChild(strawberry);
        this.render.stage.addChild(this.elements);
        const smallTextStyle = new PIXI.TextStyle({
            fill: '#fff9d8',
            fontFamily: '"Trebuchet MS", Helvetica, sans-serif',
            fontSize: 36,
            fontWeight: 'lighter',
        });
        const smallTextLabel = 'Make sure it\'s actually running.';
        const smallText: PIXI.Text = new PIXI.Text(smallTextLabel, smallTextStyle);
        smallText.y = this.render.screen.height / 1.1;
        smallText.name = 'smallText';
        let suffix = '';
        let loops = 0;
        let ticks = 0;
        this.render.ticker.add((delta) => {
            if (ticks > 500 && !this.elements.getChildByName('smallText')) {
                this.elements.addChild(smallText);
            }
            strawberry.rotation += 0.1 * delta;
            loops++;
            if (loops % 25 === 0) {
                suffix += '.';
                if (suffix === '....') {
                    suffix = '';
                }
            }
            if (loops === 2000) {
                smallText.text = this.smallTexts[Math.floor(Math.random() * this.smallTexts.length)];
                loops = 0;
            }
            if (!this.socket.connected) {
                if (strawberry.y < this.render.screen.height / 3) {
                    strawberry.y += 3;
                }
                if (text.y > this.render.screen.height / 1.4) {
                    text.y -= 3;
                }
                smallText.x = strawberry.x - smallText.width / 2;
            } else {
                strawberry.y -= 3;
                text.y += 3;
                smallText.y += 3;
            }
            ticks++;
            text.text = label + suffix;
        });
    }
}
