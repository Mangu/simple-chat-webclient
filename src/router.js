import Vue from 'vue';
import Router from 'vue-router';
import Chat from './views/Chat.vue';
import Settings from './views/Settings.vue';

Vue.use(Router); 

const router = new Router({
  routes: [       
    { path: '/Chat', component: Chat},
    { path: '/Settings', component: Settings},    
  ]
});

const originalPush = Router.prototype.push;
Router.prototype.push = function push(location) {
  return originalPush.call(this, location).catch(err => {
    if (err.name !== 'NavigationDuplicated') {
      throw err;
    }
  });
};
export default router;