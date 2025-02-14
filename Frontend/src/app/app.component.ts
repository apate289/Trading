import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { ApiserviceService } from './service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  newdata:any;

  constructor(private _apiservice:ApiserviceService) { }

  ngOnInit() {
	this.getData();
  }

  getData() {
	  this._apiservice.getdata().subscribe(res=>{this.newdata=res;})
  }
}