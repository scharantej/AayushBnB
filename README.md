 ## **AayushBNB: Flask Application Design**

### **HTML Files**

**1. index.html (Homepage)**
- This is the main page of the application.
- It displays a welcome message and provides links to the login and registration pages.

**2. login.html (Login Page)**
- This page allows users to log in to their accounts.
- It includes fields for entering the username and password, as well as a submit button.

**3. register.html (Registration Page)**
- This page allows users to create new accounts.
- It includes fields for entering the username, email, and password, as well as a submit button.

**4. dashboard.html (Dashboard Page)**
- This page is displayed after a user successfully logs in.
- It provides access to various features of the application, such as creating listings, managing bookings, and viewing messages.

**5. listing.html (Listing Page)**
- This page displays information about a specific listing.
- It includes details such as the property name, location, description, and price.

**6. booking.html (Booking Page)**
- This page allows users to book a listing.
- It includes fields for selecting the check-in and check-out dates, as well as the number of guests.

**7. message.html (Message Page)**
- This page allows users to send and receive messages to other users.
- It includes a list of messages and a form for composing new messages.

### **Routes**

**1. @app.route('/') (Homepage)**
- This route displays the index.html page.

**2. @app.route('/login') (Login Page)**
- This route displays the login.html page.

**3. @app.route('/register') (Registration Page)**
- This route displays the register.html page.

**4. @app.route('/dashboard') (Dashboard Page)**
- This route displays the dashboard.html page.

**5. @app.route('/listing/<listing_id>') (Listing Page)**
- This route displays the listing.html page for the specified listing.

**6. @app.route('/booking/<listing_id>') (Booking Page)**
- This route displays the booking.html page for the specified listing.

**7. @app.route('/message') (Message Page)**
- This route displays the message.html page.

**8. @app.route('/api/login') (Login API)**
- This route handles the login process and returns a JSON response with the user's information.

**9. @app.route('/api/register') (Registration API)**
- This route handles the registration process and returns a JSON response with the user's information.

**10. @app.route('/api/create_listing') (Create Listing API)**
- This route handles the creation of a new listing and returns a JSON response with the listing's information.

**11. @app.route('/api/book_listing') (Book Listing API)**
- This route handles the booking of a listing and returns a JSON response with the booking's information.

**12. @app.route('/api/send_message') (Send Message API)**
- This route handles the sending of a message and returns a JSON response with the message's information.

### **Additional Notes**

- The HTML files and routes provided are just a basic structure for the application.
- You may need to add additional HTML files and routes to implement specific features or customize the application to your liking.
- The design of the application can be further enhanced by adding CSS stylesheets and JavaScript files.