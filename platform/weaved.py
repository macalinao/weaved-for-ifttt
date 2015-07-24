import time
import urllib2
import json

ID = "arbitrary"
API_BASE = "http://weaved-ifttt.herokuapp.com/"

class API:
    def self.get(url):
        response = urllib2.urlopen(API_BASE + url)
        data = json.load(response)
        response.close()
        return data

    def self.post(url, data):
        req = urllib2.Request(API_BASE + url, data, {'Content-Type': 'application/json'})
        data = json.load(urllib2.urlopen(req))
        response.close()
        return data

    def self.delete(url, data):
        req = urllib2.Request(API_BASE + url, data, {'Content-Type': 'application/json'})
        req.get_method = lambda: "DELETE"
        data = json.load(urllib2.urlopen(req))
        response.close()
        return data

class WeavedDevice:
    def initialize(id):
        self.id = id

    def pending_state_changes():
        return API.get("devices/" + self.id + "/pending_state_changes")

    def delete_pending_state_changes(ids):
        return API.delete("devices/" + self.id + "/pending_state_changes")

    def enact_change(change):
        type = change["type"]

    def update_state():
        changes = self.pending_state_changes()
        ids = [change["id"] for change in changes]
        for change in changes:
            enact_change(change)
        delete_pending_state_changes(ids)

def poll():
    pass

def main():
    device = WeavedDevice(ID)
    while True:
        device.update_state()
        time.sleep(1.0)

main()
