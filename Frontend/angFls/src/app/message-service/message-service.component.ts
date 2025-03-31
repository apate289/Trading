import { HttpClient } from '@angular/common/http';
import { Component, Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})

@Component({
  selector: 'app-message-service',
  imports: [],
  templateUrl: './message-service.component.html',
  styleUrl: './message-service.component.css'
})
export class MessageServiceComponent {

  private apiUrl = 'http://localhost:5000'; // Flask backend URL

  constructor(private http: HttpClient) { }

  sendMessage(message: string): Observable<any> {
    return this.http.post<any>(`${this.apiUrl}/send_message`, { message });
  }

}
