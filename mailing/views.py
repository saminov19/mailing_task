from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
import requests
from .models import Mailing, Client, Message
from .serializers import MailingSerializer, ClientSerializer, MessageSerializer

# Client views

@api_view(['GET', 'POST'])
def client_list_create(request):
    if request.method == 'GET':
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def client_retrieve_update_destroy(request, pk):
    try:
        client = Client.objects.get(pk=pk)
    except Client.DoesNotExist:
        return Response(status=404)
    
    if request.method == 'GET':
        serializer = ClientSerializer(client)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ClientSerializer(client, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    elif request.method == 'DELETE':
        client.delete()
        return Response(status=204)

# Mailing views

@api_view(['GET', 'POST'])
def mailing_list_create(request):
    if request.method == 'GET':
        mailings = Mailing.objects.all()
        serializer = MailingSerializer(mailings, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = MailingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def mailing_retrieve_update_destroy(request, pk):
    try:
        mailing = Mailing.objects.get(pk=pk)
    except Mailing.DoesNotExist:
        return Response(status=404)
    
    if request.method == 'GET':
        serializer = MailingSerializer(mailing)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = MailingSerializer(mailing, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    elif request.method == 'DELETE':
        mailing.delete()
        return Response(status=204)

# Message views

@api_view(['GET', 'POST'])
def message_list_create(request):
    if request.method == 'GET':
        messages = Message.objects.all()
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def message_retrieve_update_destroy(request, pk):
    try:
        message = Message.objects.get(pk=pk)
    except Message.DoesNotExist:
        return Response(status=404)
    
    if request.method == 'GET':
        serializer = MessageSerializer(message)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = MessageSerializer(message, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    elif request.method == 'DELETE':
        message.delete()
        return Response(status=204)


def send_message_to_external_api(message):
    # sending messages to the external API
    # Replace the URL and payload with the actual API endpoint and data structure
    url = "https://api.example.com/send_message"
    payload = {
        'message': message.text,
        'recipient': message.client.email
    }
    headers = {
        'Content-Type': 'application/json'
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()  # Raise exception for non-2xx status codes
        return True
    except requests.exceptions.RequestException:
        return False

def send_message(request, message_id):
    # Retrieve the message object
    message = get_object_or_404(Message, pk=message_id)
    
    # Send the message to the external API
    success = send_message_to_external_api(message)
    
    if success:
        return JsonResponse({'status': 'success', 'message': 'Message sent successfully'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Failed to send message'})