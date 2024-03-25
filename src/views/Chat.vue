<template>
  <div class="page-container">
    <h3>Chat</h3>
    <div v-if="isSending" class="thinking-animation">Thinking...</div>
      <div class="messages" ref="messages">
        <div v-for="(message, index) in messages" :key="index" :class="`chat-bubble ${message.sender}`">
          <p v-html="message.text"></p>
          <span class="sender">{{ message.sender }}</span>
        </div>
      </div>    
    <div class="form-group">
        <input v-model="userInput" class="form-control long-input" placeholder="How can I help you today?" @keyup.enter="sendMessage">
    </div>
    <div class="button-container">
      <button @click="sendMessage" class="btn btn-primary">Go</button>
      <button @click="clearMessage" class="btn btn-primary">Clear</button>
      <button @click="getThread" class="btn btn-primary">New Thread</button>
      <div class="status-container">{{ status }}</div>
    </div>
  </div>
</template> 

<script>
  import assistantService from '../services/assistantService';
 
  export default {
    name: 'Chat',
    data() {
      return {
        userInput: '',
        status: '',
        messages: [],
        isSending: false,
       
      };
    },
    methods: {
      async sendMessage() {
        this.isSending = true;
        let message = this.userInput 
        this.userInput = '';
        this.messages.push({ text: message, sender: 'user' });
        this.scrollToBottom();
       
        let response = '';

        try 
        {
          response = await assistantService.postMessage(message + ' thread_id: ' + this.thread, this.thread);
          
          if (response == null) {
            response = "Sorry, I'm having trouble communicating with the assistant. Create a new thread and try again.";
          }

          console.log('Response:', response);
          this.messages.push({ text: response, sender: 'assistant' });
          this.scrollToBottom();
        }
        catch (error) {
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
        try {
          this.thread = await assistantService.getThread();         
          this.status = 'Thread: ' + this.thread;
        } catch (error) {
          console.log('Error:', error);
          this.status = 'Error: ' + error;
        }            
        this.status = 'Thread: ' + this.thread + ' ';
      },
      scrollToBottom() {
      this.$nextTick(() => {
        this.$refs.messages.scrollTop = this.$refs.messages.scrollHeight;
      });
    },
    },
    async mounted() {
          await this.getThread();
    },
  };
</script>  

<style scoped>
  .button-container {
    display: flex;
    margin-right: 10px;    
  }
  .button-container button {
    margin-right: 10px;
  }
  .page-container {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    height: 90vh; /* This will make the container take up the full viewport height */
  }
  .messages {
    flex: 1;
    overflow-y: auto;
    display: flex;
    flex-direction: column; /* Changed from column-reverse to column */
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
  .thinking-animation {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100px;
  }
  .status-container {
    background-color: beige;
  }
</style>