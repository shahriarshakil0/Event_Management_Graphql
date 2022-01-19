import graphene
from graphene_django import DjangoObjectType
from .models import *
from django.contrib.auth import get_user_model


class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()
        # fields = ("id", 'email')


class LocationType(DjangoObjectType):
    class Meta:
        model = Location


class EventType(DjangoObjectType):
    class Meta:
        model = Event


class EventMemberType(DjangoObjectType):
    class Meta:
        model = Event_member


class CreateEvent(graphene.Mutation):
    event = graphene.Field(EventType)

    class Arguments:
        name = graphene.String(required=True)
        description = graphene.String(required=True)
        location = graphene.Int(required=True)

    def mutate(self, info, name, description, location):
        location = Location.objects.get(id=location)
        event = Event(name=name, description=description, location=location)
        event.save()
        return CreateEvent(event=event)


class AddEventMember(graphene.Mutation):
    eventmember = graphene.Field(EventMemberType)

    class Arguments:
        eventid = graphene.Int(required=True)
        userid = graphene.Int(required=True)

    def mutate(self, info, eventid, userid):
        event = Event.objects.filter(id=eventid).first()
        user = get_user_model().objects.filter(id=userid).first()
        if event and user:
            eventmember = Event_member.objects.filter(event=event).first()
            if eventmember:
                eventmember.user.add(user)
                eventmember.save()
                return AddEventMember(eventmember=eventmember)
            else:
                eventmembers = Event_member.objects.create(event=event)
                eventmembers.user.add(user)
                eventmembers.save()
                return AddEventMember(eventmember=eventmembers)
        else:
            raise Exception("Event or User Not Found")


class DelateEventMember(graphene.Mutation):
    eventmember = graphene.Field(EventMemberType)

    class Arguments:
        eventid = graphene.Int(required=True)
        userid = graphene.Int(required=True)

    def mutate(self, info, eventid, userid):
        event = Event.objects.filter(id=eventid).first()
        user = get_user_model().objects.filter(id=userid).first()
        if event and user:
            eventmember = Event_member.objects.filter(
                event=event).filter(user=user).first()
            if eventmember:
                eventmember.user.remove(user)

                return DelateEventMember(eventmember=eventmember)
            else:
                raise Exception("User Not not in this Event")
            return DelateEventMember(eventmember=eventmember)
        else:
            raise Exception("Event or User Not Found")


class UpdateEventLocation(graphene.Mutation):
    location = graphene.Field(LocationType)

    class Arguments:
        eventid = graphene.Int()
        latitude = graphene.Float()
        altitude = graphene.Float()

    def mutate(slef, info, eventid, latitude, altitude):
        location = Location.objects.filter(event__id=eventid).first()
        if location:
            location.Altitude = altitude
            location.Latitude = latitude
            location.save()
            return UpdateEventLocation(location=location)
        else:
            raise Exception("Location Not Found For this Event")


class Query(graphene.ObjectType):
    event_members = graphene.List(
        UserType, eventid=graphene.Int(required=True))
    user_events = graphene.List(EventType, userid=graphene.Int(required=True))

    def resolve_event_members(self, info, eventid):
        return get_user_model().objects.filter(event_member__event=eventid)

    def resolve_user_events(self, info, userid):
        return Event.objects.filter(event_member__user__id=userid)


class Mutation(graphene.ObjectType):
    create_event = CreateEvent.Field()
    add_event_member = AddEventMember.Field()
    delate_event_member = DelateEventMember.Field()
    update_event_location = UpdateEventLocation.Field()
