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
                localStorage.setItem('assistantInstructions', this.assistantInstructions);  
                localStorage.setItem('Endpoint', this.apiEndpoint);  
                localStorage.setItem('EndpointKey', this.apiEndpointKey);                              
            },
        },
    };
</script>