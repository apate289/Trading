import { NgIf } from '@angular/common';
import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';
//import { Router } from 'express';
import { Router, RouterLink } from '@angular/router';
import { error } from 'console';
//import { UserProfileComponent } from '../user-profile/user-profile.component';
//import { MatButtonModule } from '@angular/material/button';
//import { MatFormFieldModule } from '@angular/material/form-field';
//import { MatInputModule } from '@angular/material/input';

@Component({
  selector: 'app-userlogin',
  imports: [RouterLink,ReactiveFormsModule,NgIf],
  templateUrl: './userlogin.component.html',
  styleUrl: './userlogin.component.css'
})

export class UserloginComponent implements OnInit{
  userInput : FormGroup;
  userLogin : any;
  isLoggedIn : any;
  isLoggedOut : any;

  constructor(private http: HttpClient, private router: Router) { 
        this.userInput = new FormGroup({
            userName: new FormControl('', [Validators.required, Validators.email]),
            password: new FormControl('', [Validators.required, Validators.email])
         });
      }
  ngOnInit(): void {
    //throw new Error('Method not implemented.');
    
  }

  onSubmit() {/*
    this.http.post('http://localhost:5000/login', this.userInput.value)
    .subscribe((response)=>{
      this.router.navigate(['/home']);
      //console.log(response)
      //console.log('Login Data...', this.userInput.value)
    },
    error=>{
      console.error('Login failed', error);
    })*/
  }

  login() {
    this.http.post('http://localhost:5000/login', this.userInput.value)
    .subscribe((res) => {
        // Store token or session info if needed
        this.router.navigate(['/home']);
        //if(res['status']== 200)
        this.isLoggedIn = 'True';
        //dataArray.filter(item => item.status === 200 || item.status === 201);
        //a = res.(item => item.status===200)
        console.log(res);
      },
      error => {
          // Handle login error
          console.error('Login failed', error);
      }
    );
   }

   logout() {
    //console.log('Logout failed');  
    this.http.post('http://localhost:5000/logout', this.userInput.value)
    .subscribe((res) => {
        // Store token or session info if needed
        this.router.navigate(['/home']);
        //if(res['status']== 200)
        this.isLoggedOut = 'True';
        //dataArray.filter(item => item.status === 200 || item.status === 201);
        //a = res.(item => item.status===200)
        console.log(res);
      },
      error => {
          // Handle login error
          console.error('Login failed', error);
      }
    );

   }

 }

