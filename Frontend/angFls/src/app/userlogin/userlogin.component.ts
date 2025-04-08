import { HttpClient } from '@angular/common/http';
import { Component } from '@angular/core';
//import { Router } from 'express';
import { Router, RouterLink } from '@angular/router';
//import { UserProfileComponent } from '../user-profile/user-profile.component';

@Component({
  selector: 'app-userlogin',
  imports: [RouterLink],
  templateUrl: './userlogin.component.html',
  styleUrl: './userlogin.component.css'
})

export class UserloginComponent {
  username = '';
  password = '';
  constructor(private http: HttpClient, private router: Router) { }

  ngOnInit(): void { }
   
  login() {
      this.http.post<any>('http://localhost:5000/login', { username: this.username, password: this.password })
          .subscribe(
              response => {
                  // Store token or session info if needed
                  this.router.navigate(['/home']);
              },
              error => {
                  // Handle login error
                  console.error('Login failed', error);
              }
          );
  }
  

}
