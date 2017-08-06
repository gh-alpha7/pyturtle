import turtle

turtle.color("blue")

dp=[1,2]

for i in range (2,1000):
    dp.append(dp[i-1]+dp[i-2])

for i in range (1,1000):
    turtle.circle(dp[i],180)
