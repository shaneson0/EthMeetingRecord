import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Person from '@/components/person'
import meetingRecord from '@/components/MeetingRecord'
import showMeetingRecord from '@/components/showMeetingRecord'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/person',
      name: 'person',
      component: Person
    },
    {
      path: '/meetingRecord',
      name: 'meetingRecord',
      component: meetingRecord
    },
    {
      path: '/showMeetingRecord',
      name: 'showMeetingRecord',
      component: showMeetingRecord
    }
  ]
})
