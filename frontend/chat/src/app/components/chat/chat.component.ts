import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { WebSocketService } from '../../services/websocket.service';

@Component({
  selector: 'app-chat',
  imports: [CommonModule, FormsModule],
  templateUrl: './chat.component.html',
  styleUrl: './chat.component.scss'
})
export class ChatComponent {
  public message: string = '';
  public chatHistory: string[] = [];

  constructor(private webSocketService: WebSocketService) {}

  ngOnInit(): void {
    this.webSocketService.connect();

    this.webSocketService.receiveMessage().subscribe((msg: string) => {
      this.chatHistory.push(msg);
    });
  }

  sendMessage(): void {
    if (this.message.trim()) {
      this.chatHistory.push(`Você: ${this.message}`);
      this.webSocketService.sendMessage(this.message);
      this.message = '';
    }
  }
}
