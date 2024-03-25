<template>
    <div class="page-container">
        <h3>Settings</h3>
        <form @submit.prevent="saveSettings" class="form-container">
            <div class="form-group">
                <label>Assitant Instructions</label>
                <textarea v-model="assistantInstructions" class="form-control long-input tall-textarea">needs to be write up to a modify assistant api call. added the ui as a reminder</textarea>
            </div> 
            <div class="form-group">
                <label>Assistant REST API Endpoint</label>
                <input v-model="apiEndpoint" class="form-control long-input" placeholder="API Endpoint">            
            </div>
            <div class="form-group">
                <label>Assistant REST API Key</label>
                <input v-model="apiEndpointKey" class="form-control long-input" placeholder="API Endpoint">            
            </div>                  
             
            <div class="form-group full-width">          
                <button type="submit" class="btn btn-primary">Save</button> 
            </div>
        </form>
        <div class="modal" v-if="showModal">
            <div class="modal-content">
            <span class="close-button" @click="showModal = false">&times;</span>
            <p>{{ modalMessage }}</p>
            </div>
        </div>
    </div>    
</template>
<style scoped>
    .container {
    display: flex;
    flex-direction: column;
    }
    @media (min-width: 600px) {
    .container {
        flex-direction: row;
    }
    }

    .tall-textarea {
        height: 200px;  
    }
    .form-container {
        display: grid;
        grid-template-columns: 1fr;
        gap: 10px;
    }
    .form-group {
        
        box-sizing: border-box; 
        width: 100%;
    }
    .tall-textarea {
        flex-basis: 100%;
    }

    .checkbox-left {
        display: block;
        width: auto;
        transform: scale(3);
        margin-left: 15px;
    }
    .modal {
        display: flex;
        justify-content: center;
        align-items: center;
        position: fixed;
        z-index: 1;
        left: 0;
        top: 0;
        width: 100%;
        height: 100%;
        overflow: auto;
        background-color: rgba(0,0,0,0.4);
    }

    .modal-content {
        background-color: #fefefe;
        margin: auto;
        padding: 20px;
        border: 1px solid #888;
        width: 80%;
    }
    .close-button {
        color: #aaa;
        float: right;
        font-size: 28px;
        font-weight: bold;
    }

    .close-button:hover,
    .close-button:focus {
    color: black;
    text-decoration: none;
    cursor: pointer;
    }
</style>

<script>
    import DOMPurify from 'dompurify';

    export default {
        data() {
            return {
                assistantInstructions: '',
                apiEndpoint: '',
                apiEndpointKey: '',                               
                checkboxValue: false, 
                showModal: false,
                modalMessage: '',    
            };
        },
        watch: {
            assistantInstructions(newVal) {
                this.assistantInstructions = DOMPurify.sanitize(newVal);
            },
            apiEndpoint(newVal) {
                //this.apiEndpoint = DOMPurify.sanitize(newVal);
            },
            apiEndpointKey(newVal) {
                this.apiEndpointKey = DOMPurify.sanitize(newVal);
            }
        },  
        created() {
            this.assistantInstructions = localStorage.getItem('assistantInstructions') || '';
            this.apiEndpoint = localStorage.getItem('Endpoint') || '';
            this.apiEndpointKey = localStorage.getItem('EndpointKey') || '';
            
        },
        methods: {
            saveSettings() {
                try {
                    localStorage.setItem('assistantInstructions', this.assistantInstructions);  
                    localStorage.setItem('Endpoint', this.apiEndpoint);  
                    localStorage.setItem('EndpointKey', this.apiEndpointKey); 
                    this.modalMessage = 'Settings were saved successfully.';
                    this.showModal = true; 
                } catch (e) {
                    this.modalMessage = 'Failed to save settings.';
                    this.showModal = true;
                }                            
            },
        },
    };
</script>