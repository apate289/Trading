import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, FormsModule, Validator } from '@angular/forms';
//import { Router } from 'express';
import { Router } from '@angular/router';
import { ReactiveFormsModule } from '@angular/forms';


@Component({
  selector: 'app-user-profile',
  imports: [FormsModule, ReactiveFormsModule],
  templateUrl: './user-profile.component.html',
  styleUrl: './user-profile.component.css'
})
export class UserProfileComponent implements OnInit {
  input: FormGroup;
  username: string = '';
  profile: any;
  msg = 'We are in user-profile....'

  constructor(private http: HttpClient, private router: Router) {
      this.input = new FormGroup({
          userName: new FormControl(''),
          FirstName: new FormControl(''),
          LastName: new FormControl(''),
          mobile: new FormControl(''),
          email: new FormControl(''),
          address: new FormControl(''),
          city: new FormControl(''),
          state: new FormControl(''),
          country: new FormControl(''),
          postalcode: new FormControl(''),
          password: new FormControl('')
    });
   }

  ngOnInit(): void {
    this.profile = '/login'; //'/api/submit';
  }

  
  onSubmit() {
      this.http.post('http://localhost:5000/register', this.input.value)//, { headers: headers })
      .subscribe(() =>
          console.log('Form submitted 1...', this.input.value)
          //this.router.navigate(['/login'])
      );
    // Handle form submission logic here
    console.log('Form submitted', this.input);
  }
  
  public register() {

   }
  
}