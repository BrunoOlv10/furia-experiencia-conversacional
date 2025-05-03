import { Component, OnInit, ViewChild, ElementRef } from '@angular/core';
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
  public isLoading: boolean = false;

  @ViewChild('chatScrollHistory') private chatScrollHistory: ElementRef | undefined;

  constructor(private webSocketService: WebSocketService) {}

  ngOnInit(): void {
    this.webSocketService.connect();

    this.webSocketService.receiveMessage().subscribe((msg: string) => {
      this.chatHistory.push(msg);
      this.isLoading = false;
      this.scrollToBottom();
    });
  }

  sendMessage(): void {
    if (this.message.trim()) {
      this.chatHistory.push(`Você: ${this.message}`);
      this.isLoading = true;
      this.webSocketService.sendMessage(this.message);
      this.message = '';
      this.scrollToBottom();
    }
  }

  private scrollToBottom(): void {
    setTimeout(() => {
      if (this.chatScrollHistory) {
        this.chatScrollHistory.nativeElement.scrollTop = this.chatScrollHistory.nativeElement.scrollHeight;
      }
    }, 100);
  }
}
