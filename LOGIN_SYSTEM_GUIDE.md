# 🔐 SijaisX Login System Implementation Guide

## 🎯 **What We've Built**

I've implemented a complete login system with session management and user-based routing for your SijaisX application! Here's what's now working:

### ✅ **Completed Features**

1. **✨ Login Form with Validation**
   - Email and password validation
   - Loading states during login
   - Error handling and user feedback
   - Redirect to registration page

2. **🔒 Session Management**
   - User data stored in localStorage
   - Session persists until manual logout
   - Automatic session validation

3. **🛡️ Protected Routes**
   - Teachers can only access `/opettajille`
   - Substitutes can only access `/sijaisille`
   - Automatic redirection based on user role

4. **👤 User Authentication Flow**
   - Login → Validate → Store Session → Redirect by Role
   - Logout → Clear Session → Redirect to Home

---

## 🏗️ **How It Works**

### **1. Login Process Flow**

```
User enters email/password
         ↓
Frontend calls login API
         ↓
Backend checks database (Teacher & Substitute tables)
         ↓
If valid: Return {user_ID, role}
         ↓
Frontend stores user data in localStorage
         ↓
Redirect to appropriate page based on role
```

### **2. Authentication Components**

**📁 `frontend/src/functions/auth.ts`**
- `isAuthenticated()` - Check if user is logged in (no time expiry)
- `getCurrentUser()` - Get current user data
- `logout()` - Clear session and redirect
- `hasRole()` - Check user role
- `getUserID()` - Get user ID

**📁 `frontend/src/components/ProtectedRoute.tsx`**
- Wraps pages that require authentication
- Automatically redirects unauthorized users
- Role-based access control

**📁 `frontend/src/components/Login/loginForm.tsx`**
- Complete login form with validation
- Calls backend API
- Handles success/error states
- Stores session data

**📁 `frontend/src/components/UserInfo.tsx`**
- Displays current user information
- Logout functionality
- Can be added to any protected page

---

## 🧪 **How to Test the Login System**

### **Step 1: Start the Backend Server**
```bash
cd backend
python -m src.api_calls
```
*Server should start on http://localhost:5000*

### **Step 2: Start the Frontend**
```bash
cd frontend
npm run dev
# or
pnpm dev
```
*Frontend should start on http://localhost:5173*

### **Step 3: Test Registration**
1. Go to `/register`
2. Register a new teacher or substitute
3. Note the email and password you used

### **Step 4: Test Login**
1. Go to `/login`
2. Enter the email and password from registration
3. Should redirect to:
   - **Teachers**: `/opettajille`
   - **Substitutes**: `/sijaisille`

### **Step 5: Test Protected Routes**
1. Try accessing `/opettajille` without logging in → Should redirect to `/login`
2. Login as substitute, try accessing `/opettajille` → Should redirect to `/sijaisille`
3. Login as teacher, try accessing `/sijaisille` → Should redirect to `/opettajille`

### **Step 6: Test Session Management**
1. Login successfully
2. Refresh the page → Should stay logged in
3. Check browser localStorage → Should see `sijaisx_user` data
4. Logout → Should clear localStorage and redirect to home

---

## 🔧 **How to Add Logout to Your Pages**

Add the UserInfo component to any protected page:

```tsx
import UserInfo from '../UserInfo';

const YourPage = () => {
  return (
    <div>
      <UserInfo /> {/* Shows user info + logout button */}
      {/* Your existing page content */}
    </div>
  );
};
```

---

## 🎨 **How to Customize User Experience**

### **1. Add User Information to Pages**

```tsx
import { getCurrentUser, getUserID } from '../functions/auth';

const YourComponent = () => {
  const user = getCurrentUser();
  const userID = getUserID();
  
  return (
    <div>
      <h1>Welcome, {user?.email}!</h1>
      <p>Your role: {user?.role}</p>
      <p>Your ID: {userID}</p>
    </div>
  );
};
```

### **2. Role-based Content**

```tsx
import { hasRole } from '../functions/auth';

const YourComponent = () => {
  const isTeacher = hasRole('teacher');
  const isSubstitute = hasRole('substitute');
  
  return (
    <div>
      {isTeacher && <TeacherOnlyContent />}
      {isSubstitute && <SubstituteOnlyContent />}
    </div>
  );
};
```

---

## 🚀 **Next Steps & Improvements**

### **1. Enhanced Security (Optional)**
- Add password hashing in backend
- Implement JWT tokens instead of localStorage
- Add password reset functionality

### **2. Better User Experience**
- Remember last visited page before login
- Add "Remember Me" option
- Profile picture upload and display

### **3. Database Enhancements**
- Add last login timestamp
- Track user activity
- Add user preferences

---

## 🐛 **Troubleshooting**

### **Common Issues:**

**🔴 "Invalid credentials" error**
- Check if user is registered in database
- Verify email/password match exactly
- Check backend server is running

**🔴 "Not redirecting after login"**
- Check browser console for errors
- Verify frontend can reach backend API
- Check localStorage for user data

**🔴 "Protected routes not working"**
- Clear localStorage and try again
- Check browser console for routing errors
- Verify ProtectedRoute component is imported correctly

### **Debug Commands:**

```javascript
// In browser console, check current user:
JSON.parse(localStorage.getItem('sijaisx_user'))

// Clear session manually:
localStorage.removeItem('sijaisx_user')

// Check if authenticated:
// (run this in a component)
import { isAuthenticated } from './functions/auth';
console.log('Is authenticated:', isAuthenticated());
```

---

## 📊 **Database Schema Reference**

Your login system works with these database tables:

```sql
-- Teachers
Teacher {
  teacher_ID: TEXT PRIMARY KEY
  email: TEXT UNIQUE
  password: TEXT
  name: TEXT
  phone_number: TEXT
  school_ID: TEXT
}

-- Substitutes  
Substitute {
  substitute_ID: TEXT PRIMARY KEY
  email: TEXT UNIQUE
  password: TEXT
  name: TEXT
  phone_number: TEXT
  experience: INTEGER
}
```

---

## 🎉 **Congratulations!**

You now have a fully functional login system with:
- ✅ User authentication
- ✅ Session management  
- ✅ Role-based routing
- ✅ Protected pages
- ✅ Logout functionality

Your users can now:
1. **Register** as teacher or substitute
2. **Login** with their credentials
3. **Access role-specific pages**
4. **Stay logged in** across page refreshes
5. **Logout** when done

The system automatically directs teachers to teacher pages and substitutes to substitute pages, keeping your application secure and user-friendly!