import { NgFor } from '@angular/common';
import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-cap',
  imports: [NgFor],
  templateUrl: './cap.component.html',
  styleUrl: './cap.component.css'
})
export class CapComponent implements OnInit{

  newdata :any;

  constructor(private http: HttpClient){
   
  }

  ngOnInit() {
    this.http.get('http://localhost:5000/cap').subscribe(
      cap=> {
        this.newdata=cap;
        console.log(this.newdata)
      }//console.log(cap)
    )
  }

}
