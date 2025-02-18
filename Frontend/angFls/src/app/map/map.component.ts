import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-map',
  imports: [],
  templateUrl: './map.component.html',
  styleUrl: './map.component.css'
})
export class MapComponent implements OnInit {

  maper = 'Ankit'; 
  Cars:any;
  constructor() {}

  ngOnInit() {
    this.Cars = localStorage.getItem('Cars')  ;
    }

  changecar(event :Event) {
    const {target} = event;
    //this.selected = value
    console.log("you are in MAP Component");  
    if (target) console.log((target as HTMLButtonElement).value);
    localStorage.setItem('Cars',(target as HTMLButtonElement).value);
    //window.location.reload()

  }
}
