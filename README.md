# Django Event Management

> Create a new event for multiple members.

```python
mutation CreateEvent($name:String!,$description:String!,$location:Int!) {
  createEvent(name:$name,description:$description,location:$location){
    event{
      id
      name
      description
      location{
        id
        Altitude
        Latitude
      }
    }
  }
}

mutation addEventMember($eventid: Int!,$userid: Int!){
  addEventMember(eventid: $eventid,userid: $userid){
    eventmember{
      id
      user{
        id
      }
      event{
        id
      }
    }
  }
}
```

> Delete any members from an event

```python
mutation delateEventMember($eventid: Int!, $userid: Int!) {
  delateEventMember(eventid: $eventid, userid: $userid) {
    eventmember {
      id
      user {
        id
      }
      event {
        id
      }
    }
  }
}
```

> Update a location for an event

```python
mutation updateEventLocation($altitude: Float!,$eventid: Int!,$latitude: Float!) {
  updateEventLocation(altitude: $altitude,eventid: $eventid,latitude:$latitude) {
   	location{
      id
      Latitude
      Altitude
    }
  }
}

```

> Query an event for all members

```python
query eventMembers($eventid: Int!){
  eventMembers(eventid:$eventid){
    id
  }
}
```

> Query all events for a single user

```python
query userEvents($userid: Int!){
  userEvents(userid:$userid){
    id
  }
}
```
