import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-cap',
  imports: [],
  templateUrl: './cap.component.html',
  styleUrl: './cap.component.css'
})
export class CapComponent implements OnInit{

  constructor(private http: HttpClient){
   
  }

  ngOnInit() {
    this.http.get('http://localhost:5000/').subscribe(
      cap=> console.log(cap)
    )
  }

}
