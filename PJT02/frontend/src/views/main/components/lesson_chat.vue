<template>
  <div id="chatContainer">
    <div id="chatComponent">
      <div id="chatToolbar">
        <span> CHAT</span>
        <button @click="close" id="closeButton">
          <span>채팅창</span>
        </button>
      </div>
      <!-- #chatScroll -->
      <div class="message-wrap" >
        <div v-for="data in this.messagelist" :key="data" class="message">
          <!-- <img class="user-img" [src]="data.userAvatar" /> -->
          <div class="msg-detail">
            <!-- 메시지 작성자 -->
            <div class="msg-info">
              <p>{{ data.nickname }}</p>
            </div>
            <!-- 메시지 -->
            <div class="msg-content">
              <span class="triangle"></span>
              <p class="text">{{data.message}}</p>
            </div>
          </div>
        </div>
      </div>

      <div id="messageInput">
          <!-- #chatInput -->
        <input
          placeholder="Send a message"
          autocomplete="off"
          @enter="sendMessage"
          id="chatInput"
        />
        <button id="sendButton" @click="sendMessage">
          <span>send</span>
        </button>
      </div>
    </div>
  </div>
</template>

<script>
// import { Component, ElementRef, Input, OnInit, ViewChild, HostListener, OnDestroy } from '@angular/core';
// import { ChatService } from '../../services/chat/chat.service';
// import { ChatMessage } from '../../types/chat-type';
// import { Subscription } from 'rxjs/internal/Subscription';
// @Component({
// 	selector: 'chat-component',
// 	templateUrl: './chat.component.html',
// 	styleUrls: ['./chat.component.css']
// })
// export class ChatComponent implements OnInit, OnDestroy {
// 	@ViewChild('chatScroll') chatScroll: ElementRef;
// 	@ViewChild('chatInput') chatInput: ElementRef;

// 	@Input() lightTheme: boolean;

// 	message: string;

// 	messageList: ChatMessage[] = [];
// 	chatOpened: boolean;

// 	private chatMessageSubscription: Subscription;
// 	private chatToggleSubscription: Subscription;

// 	constructor(private chatService: ChatService) {}

// 	@HostListener('document:keydown.escape', ['$event'])
// 	onKeydownHandler(event: KeyboardEvent) {
// 		console.log(event);
// 		if (this.chatOpened) {
// 			this.close();
// 		}
// 	}

// 	ngOnInit() {
// 		this.subscribeToMessages();
// 		this.subscribeToToggleChat();
// 	}

// 	ngOnDestroy(): void {
// 		if (this.chatMessageSubscription) {
// 			this.chatMessageSubscription.unsubscribe();
// 		}
// 		if (this.chatToggleSubscription) {
// 			this.chatToggleSubscription.unsubscribe();
// 		}
// 	}

// 	eventKeyPress(event) {
// 		// Pressed 'Enter' key
// 		if (event && event.keyCode === 13) {
// 			this.sendMessage();
// 		}
// 	}

// 	sendMessage(): void {
// 		this.chatService.sendMessage(this.message);
// 		this.message = '';
// 	}

// 	scrollToBottom(): void {
// 		setTimeout(() => {
// 			try {
// 				this.chatScroll.nativeElement.scrollTop = this.chatScroll.nativeElement.scrollHeight;
// 			} catch (err) {}
// 		}, 20);
// 	}

// 	close() {
// 		this.chatService.toggleChat();
// 	}

// 	private subscribeToMessages() {
// 		this.chatMessageSubscription = this.chatService.messagesObs.subscribe((messages: ChatMessage[]) => {
// 			this.messageList = messages;
// 			this.scrollToBottom();
// 		});
// 	}

// 	private subscribeToToggleChat() {
// 		this.chatToggleSubscription = this.chatService.toggleChatObs.subscribe((opened) => {
// 			this.chatOpened = opened;
// 			if (this.chatOpened) {
// 				this.scrollToBottom();
// 				setTimeout(() => {
// 					this.chatInput.nativeElement.focus();
// 				});
// 			}
// 		});
// 	}
// }
export default {
  name: 'Chat',
  methods:{
    close(){
      this.$emit("close")
    },
   // 메세지 보내기
    sendMessage(message){
      session.connect(token, { clientData: this.userId })
        .then(session.signal({
        data: message,  // Any string (optional)
        to: [],                     // Array of Connection objects (optional. Broadcast to everyone if empty)
        type: 'my-chat'             // The type of message (optional)
        }).then(() => {
            console.log('Message successfully sent');
        }).catch(error => {
            console.error(error);
      }))
      .catch(error =>{
        console.error(error);
      });
    },
    //메세지 받기
    receiveMessage(event){
      session.connect(token, { clientData: this.userId })
      .then(session.on('signal', (event) => {
        console.log(event.data); // Message
        console.log(event.from); // Connection object of the sender
        console.log(event.type); // The type of message
      }))
      .catch(error =>{
        console.error(error);
      });
    },
    // session.on("streamCreated", function (event) {
    // session.subscribe(event.stream, "subscriber");
    // console.log("USER DATA: " + event.stream.connection.data);
    // });
  }
}
</script>

<style>
#chatContainer {
  position: absolute;
  z-index: 0;
  width: 100%;
  height: calc(100% - 20px);
}
input {
  font-family: 'Ubuntu', sans-serif;
}

#chatToolbar {
  height: 30px;
  background-color: #3d3d3d;
  box-sizing: border-box;
  font-weight: bold;
  font-size: 14px;
  text-align: center;
  padding-top: 4px;
  border-top-left-radius: 6px;
  border-top-right-radius: 6px;
  color: #ffffff;
}

#closeButton {
  position: absolute;
  right: 0;
  top: -5px;
}

#chatComponent {
  background-color: #b8b8b8;
  position: absolute;
  z-index: 99999;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  margin: auto;
  height: calc(100% - 30px);
  width: calc(100% - 30px);
  border-radius: 20px;
}

.message-wrap {
  padding: 0 15px;
  height: calc(100% - 80px);
  overflow: auto;
}

.message {
  position: relative;
  padding: 7px 0;
}
.user-img {
  position: absolute;
  border-radius: 45px;
  width: 60px;
  height: 60px;
  top: 15px;
}

.msg-detail {
  width: calc(100% - 65px);
  display: inline-block;
}

.msg-detail p {
  margin: 0;
  font-size: 15px;
}

.msg-info p {
  font-size: 0.8em;
  color: #000000;
  font-style: italic;
}

.msg-content {
  position: relative;
  margin-top: 5px;
  border-radius: 5px;
  padding: 8px;
  color: #000000;
  width: auto;
  max-width: 95%;
}

span.triangle {
  border-radius: 2px;
  height: 8px;
  width: 8px;
  top: 12px;
  display: block;
  -webkit-transform: rotate(45deg);
  transform: rotate(45deg);
  position: absolute;
}

.text {
  word-break: break-all;
}

/* Start message from other user */

.message.left .msg-detail .msg-info {
  text-align: left;
}

.message.left .msg-detail {
  padding-left: 65px;
}

.message.left .user-img {
  left: -5px;
  border: 1px solid #f0f0f094;
}

.message.left .msg-detail .msg-content {
  background-color: #f0f0f0;
  float: left;
}
.message.left .msg-detail .msg-content span.triangle {
  background-color: #f0f0f0;
  border-bottom-width: 0;
  border-left-width: 0;
  left: -5px;
}

/* End message from other user */

/* Start my messages */

.message.right .msg-detail .msg-info {
  text-align: right;
}
.message.right .user-img {
  right: -5px;
  border: 1px solid #c8ffe8ab;
}

.message.right .msg-detail .msg-content {
  background-color: #c8ffe8;
  float: right;
}
.message.right .msg-detail .msg-content span.triangle {
  background-color: #c8ffe8;
  border-bottom-width: 0;
  border-left-width: 0;
  right: -5px;
}

/* End my messages */

#messageInput {
  position: absolute;
  bottom: 0px;
  width: 100%;
  background-color: #ffffff;
  text-align: center;
  padding: 10px 0px;
  height: 30px;
  border-bottom-left-radius: 6px;
  border-bottom-right-radius: 6px;
}
#messageInput input {
  width: 90%;
  height: 100%;
  border: none;
  outline: none;
  font-size: 14px;
  margin-left: -6%;
}

#sendButton {
  background-color: #81e9b0;
  position: absolute;
  right: 10px;
  top: 0;
  bottom: 0;
  margin: auto;
  border: 1px solid #7ae2a9;
  box-shadow: none !important;
}
#sendButton mat-icon {
  margin-left: 3px !important;
  margin-bottom: 2px !important;
}

::-webkit-scrollbar {
  width: 8px;
}

::-webkit-scrollbar-thumb {
  background-color: #6b6b6b;
}

.chatComponentLight ::-webkit-scrollbar-thumb {
  background-color: #eeeeee !important;
}
</style>
