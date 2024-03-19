<template>
  <div class="page-container">
    <h3>Chat</h3>
    <div v-if="isSending" class="thinking-animation">Thinking...</div>
    <div class="messages">
      <div v-for="(message, index) in messages" :key="index" :class="`chat-bubble ${message.sender}`">
        <p>{{ message.text }}</p>
        <span class="sender">{{ message.sender }}</span>
      </div>
    </div>    
    <div class="form-group">
        <input v-model="userInput" class="form-control long-input" placeholder="How can I help you today?" @keyup.enter="sendMessage">
    </div>
    <div class="button-container">
      <button @click="sendMessage" class="btn btn-primary">Go</button>
      <button @click="clearMessage" class="btn btn-primary">Clear</button>
    </div>
  </div>
</template>  

<script>

  import assistantService from '../services/assistantService';// replace with the actual path to your module
  export default {
    name: 'Chat',
    thread:'',
    data() {
      return {
        userInput: '',
        messages: [],
        isSending: false,
      };
    },
    methods: {
      async sendMessage() {
        this.isSending = true;
        this.messages.unshift({ text: this.userInput, sender: 'user' });
        this.userInput = '';
        let response = '';

        try {
          response = await assistantService.postMessage(this.userInput, this.thread);
          if (response == null) {
            response = "Sorry, I'm having trouble communicating with the assistant. Reload to try a new thread.";
          }
          console.log('Response:', response);
          this.messages.unshift({ text: response, sender: 'assistant' });
        } catch (error) {
          console.log('Error:', error);
        } finally {
          this.isSending = false;
        }
      },
      clearMessage() {
        this.messages = [];
        this.userInput = '';        
      },
      async getThread() {
        if(this.thread == null || this.thread==''){
          this.thread = await assistantService.getThread();
          console.log('Thread:', this.thread);
        }  
      }
    },
    async mounted() {
          await this.getThread();
    },
  };
</script>  

<style scoped>
  .button-container {
    display: flex;
    justify-content: space-between;
  }
  .page-container {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    height: 90vh; /* This will make the container take up the full viewport height */
  }
  .messages {
    flex: 1;
    overflow-y: auto; /* This will add a scrollbar if the messages overflow the div */
  }
  .chat-bubble {
    background-color: #f0f0f0;
    border-radius: 5px;
    padding: 10px;
    margin: 10px 0;
    position: relative;
    color: #000000;
  }
  .sender {
    font-size: 0.8em;
    color: #888;
    position: absolute;
    bottom: 5px;
    right: 10px;
    font-weight: bold;
  }
  .user {
      background-color: #eeeeee; 
  }
  .assistant {
      background-color: #252bdc;       
      color: #ffffff;
  }
</style>