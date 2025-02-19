import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { MapComponent } from './map/map.component';
import { CapComponent } from './cap/cap.component';
import { NgFor } from '@angular/common';

@Component({
  selector: 'app-root',
  imports: [MapComponent,CapComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'Developer';
}
