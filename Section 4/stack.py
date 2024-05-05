"""Stack"""

browsing_sessions = []

browsing_sessions.append(1)
browsing_sessions.append(2)
browsing_sessions.append(3)

print(browsing_sessions)

print(browsing_sessions.pop())

if not browsing_sessions:
    print("Disable Back Button")
else:
    print("Redirected to: ", browsing_sessions[-1])

