import { Component, NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { RouterLink, RouterModule, RouterOutlet } from '@angular/router';
import { MessageServiceComponent } from './message-service/message-service.component';
import { HeaderComponent } from './header/header.component';

@Component({
  selector: 'app-root',
  imports: [FormsModule,RouterModule,HeaderComponent], 
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})

export class AppComponent {
  title = 'Developer';
  message: string = '';

  constructor(private messageService: MessageServiceComponent) {}

  sendMessage() {
    this.messageService.sendMessage(this.message).subscribe(response => {
      console.log('Message sent successfully', response);
      this.message = ''; 
    });
  }
}
