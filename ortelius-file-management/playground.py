import requests
import json

API_ENDPOINT = 'http://192.168.225.51:5000/file'

#request endpoint
def test_post():
    sample_file = [
        'IyBPcnRlbGl1cw0KDQpXZWxjb21lIHRvIE9ydGVsaXVzLiBPcnRlbGl1cyBpcyBhbiBvcGVuIHNv',
        'dXJjZSBwcm9qZWN0IHRoYXQgYWltcyB0byBzaW1wbGlmeSB0aGUgaW1wbGVtZW50YXRpb24gb2Yg',
        'bWljcm9zZXJ2aWNlcy4gQnkgcHJvdmlkaW5nIGEgY2VudHJhbCBjYXRhbG9nIG9mIHNlcnZpY2Vz',
        'IHdpdGggdGhlaXIgZGVwbG95bWVudCBzcGVjcywgYXBwbGljYXRpb24gdGVhbXMgY2FuIGVhc2ls',
        'eSBjb25zdW1lIGFuZCBkZXBsb3kgc2VydmljZXMgYWNyb3NzIGNsdXN0ZXIuIE9ydGVsaXVzIHRy',
        'YWNrcyBhcHBsaWNhdGlvbiB2ZXJzaW9ucyBiYXNlZCBvbiBzZXJ2aWNlIHVwZGF0ZXMgYW5kIG1h',
        'cHMgdGhlaXIgc2VydmljZSBkZXBlbmRlbmNpZXMgZWxpbWluYXRpbmcgY29uZnVzaW9uIGFuZCBn',
        'dWVzcyB3b3JrLiAgVW5pcXVlIHRvIE9ydGVsaXVzIGlzIHRoZSBhYmlsaXR5IHRvIHRyYWNrIHlv',
        'dXIgbWljcm9zZXJ2aWNlIGludmVudG9yeSBhY3Jvc3MgY2x1c3RlcnMgbWFwcGluZyB0aGUgZGlm',
        'ZmVyZW5jZXMuICBPcnRlbGl1cyBzZXJ2ZXMgU2l0ZSBSZWxpYWJpbGl0eSBFbmdpbmVlcnMgYW5k',
        'IENsb3VkIEFyY2hpdGVjdHMgaW4gdGhlaXIgbWlncmF0aW9uIHRvIGFuZCBvbmdvaW5nIG1hbmFn',
        'ZW1lbnQgb2YgYSBtaWNyb3NlcnZpY2UgaW1wbGVtZW50YXRpb24uIEZvciBtb3JlIGluZm9ybWF0',
        'aW9uLCBzZWUgdGhlIGNvbXByZWhlbnNpdmUgZG9jdW1lbnRhdGlvbiBhdCBodHRwOi8vZG9jcy5v',
        'cnRlbGl1cy5pbyANCg0KIyMgT3J0ZWxpdXMgTWlzc2lvbg0KDQpPdXIgbWlzc2lvbiBpcyB0byBz',
        'aW1wbGlmeSB0aGUgYWRvcHRpb24gb2YgbW9kZXJuIGFyY2hpdGVjdHVyZSB0aHJvdWdoIGEgd29y',
        'bGQtY2xhc3MgbWljcm9zZXJ2aWNlIG1hbmFnZW1lbnQgcGxhdGZvcm0gZHJpdmVuIGJ5IGEgc3Vw',
        'cG9ydGl2ZSBhbmQgZGl2ZXJzZSBnbG9iYWwgb3BlbiBzb3VyY2UgY29tbXVuaXR5Lg0KDQojIyBP',
        'cnRlbGl1cyBWYWx1ZSBTdGF0ZW1lbnRzDQoNCi0gV2Ugd2FudCBNZW1iZXJzIHRvIGxlYXJuIGFu',
        'ZCB1bmRlcnN0YW5kIHNvbHV0aW9ucyBhcm91bmQgbWljcm9zZXJ2aWNlIHVzZSBhbmQgdGhlaXIg',
        'Y2hhbGxlbmdlcyB0aHJvdWdoIGEgZGl2ZXJzZSBjb250cmlidXRvciBiYXNlLiANCi0gV2Ugd2Fu',
        'dCBvdXIgbWVtYmVycyB0byBkZXZlbG9wIHRoZWlyIGNhcmVlcnMsIHNraWxscyBhbmQgZ2FpbiBj',
        'b21tdW5pdHkgcmVjb2duaXRpb24gZm9yIHRoZWlyIHdvcmsgYW5kIGV4cGVydGlzZS4gDQotIFdl',
        'IHdhbnQgb3VyIG1lbWJlcnMgdG8gaGF2ZSB0aGUgb3Bwb3J0dW5pdHkgdG8gc2hhcmUgYW5kIHJl',
        'dXNlIG9wZW4gc291cmNlIG1pY3Jvc2VydmljZXMgdG8gZnVydGhlciB0aGUgYWRvcHRpb24gb2Yg',
        'YSBjbG91ZCBuYXRpdmUgZGV2ZWxvcG1lbnQuIA0KLSBXZSB3YW50IG1lbWJlcnMgdG8gbGVhcm4g',
        'aG93IHRvIGNvbnRyaWJ1dGUgdG8gYW4gb3BlbiBzb3VyY2UgY29tbXVuaXR5IGFuZCBiZWNvbWUg',
        'cGFydCBvZiB0aGUgYnJvYWRlciBjb252ZXJzYXRpb24gYXJvdW5kIGNsb3VkIG5hdGl2ZSBhcmNo',
        'aXRlY3R1cmUu']
    
    # sample_file1 = []
    data = {'compid': 100, 'filetype': 'readme', 'file': json.dumps(sample_file)}
    r = requests.post(url = API_ENDPOINT, data = data)
    print('Status is:%s, Response is:%s  '%(r.status_code,r.text))

# test_post()

def test_get():
    r = requests.get(url = API_ENDPOINT, params={'compid': 100, 'filetype': 'readme'})
    print('Status is:%s, Response is:%s  '%(r.status_code,r.text))

test_get()