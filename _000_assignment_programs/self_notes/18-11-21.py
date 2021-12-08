'''
1. what is authorization key ?
 it is a process to determine whether the authenticated user has access to the particular resources.
it checks tour rights to grant you access to resources such as information databases,files etc.

Authorization is the mechanism by which a system determines what level of access a particular (authenticated)
user should have access to resources controlled by the system.

Authorization is the process of granting someone to do something. It means it a way to check if the user has
permission to use a resource or not.
It defines that what data and information one user can access. It is also said as AuthZ.
The authorization usually works with authentication so that the system could know who is accessing the information.
Authorization is not always necessary to access information available over the internet. Some data available
over the internet can be accessed without any authorization.



2. what is authentication ?
it is about validating your crdentials like username and password to verify your
(identity).Authentication refers to giving a user permissions to access a particular resource.
Since, everyone can’t be allowed to access data from every URL, one would require authentication primarily.
To achieve this authentication, typically one provides authentication data through Authorization header or a custom
header defined by server.

3. authorization and authentication:?

Authentication is the process of identifying a user to provide access to a system.
Authorization is the process of giving permission to access the resources.

In this, the user or client and server are verified.
In this, it is verified that if the user is allowed through the defined policies and rules.

It is usually performed before the authorization.
It is usually done once the user is successfully authenticated.

It requires the login details of the user, such as user name & password, etc.
It requires the user's privilege or security level.

Data is provided through the Token Ids.
Data is provided through the access tokens.

Example: Entering Login details is necessary for the employees to authenticate themselves to access the organizational emails or software.

Example: After employees successfully authenticate themselves,
they can access and work on certain functions only as per their roles and profiles.


Authentication credentials can be partially changed by the user as per the requirement.
Authorization permissions cannot be changed by the user.
The permissions are given to a user by the owner/manager of the system, and he can only change it.

4. what is api?

which is a software intermediary that allows two applications to talk to each other.
Each time you use an app like Facebook, send an instant message,
or check the weather on your phone, you’re using an API.

example:When you use an application on your mobile phone, the application connects to the Internet and
sends data to a server. The server then retrieves that data, interprets it, performs the necessary actions
and sends it back to your phone. The application then interprets that data and presents you with the information
you wanted in a readable way.

4.How do I use authorization in API?


In authorization, a user or application is granted access to an API after the API determines the extent
of the permissions that it should assign. Usually, authorization occurs after identity is successfully validated
through authenticationso that the API has some idea of what sort of access it should grant.
This is what an API is - all of this happens via API.

5.How do you implement authorization?

Authorization is implemented using access tokens that must be set. A user, or the groups to which the user belongs to,
can be associated with zero-to-many access token values.

6.where we use the authorization?
Authorization is a process by which a server determines if the client has permission to use a resource or access a file.
Authorization is usually coupled with authentication so that the server
has some concept of who the client is that is requesting access.

7.why we need authorization ?
 They confirm the identity of the user and grant access to your website or application.


8.difference between swagger and postman?

Postman is the only complete API development environment, used by nearly five million developers and more than 100,000
companies worldwide. ...for small applications we can use this postman.based on input it will decide whether it is put,post method
it will provide body and header tag for data.

Swagger UI is a dependency-free collection of HTML, Javascript,
and CSS assets that dynamically generate beautiful documentation and sandbox from a Swagger-compliant API.
for bigger applications we can use swagger.swagger is not define put and post methods.
it will not provide body and header tags .
'''




