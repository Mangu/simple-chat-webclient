import axios from 'axios';

let endpoint = localStorage.getItem('apiEndpoint');
let key = localStorage.getItem('apiEndpointKey');
let assistantInstructions = localStorage.getItem('assistantInstructions');
     

export default {  
  
  async getThread() {
     console.log("getThread " + endpoint);
    try {
        const response = await axios.post(endpoint+"/thread", {},
        {
          headers: {
            access_token: key,
            'Content-Type': 'application/json',
          }
        });
        const data = response.data.thread_id;
        console.log(data);
        return data.replace(/"/g, ''); 
    
    } 
    catch (error) {
        console.error('Failed to fetch thread:', error);
    }
  },

  async postMessage(message, thread_id) {
    
    try {
      const response = await axios.post(endpoint+"/message",
        {
          message:message,
          thread_id: thread_id,
        },
        {
          headers: {
            access_token: key,
            'Content-Type': 'application/json',
          },
        }
      );
        const messageText = response.data.message.replace(/\n/g, '');
        return messageText;
    } catch (error) {
        console.error('Failed to post message:', error);
    }
}
};
