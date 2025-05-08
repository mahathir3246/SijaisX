// Import the necessary functions from Firebase SDK
import { initializeApp } from 'firebase/app';
import { getFirestore, collection, addDoc } from 'firebase/firestore';
import { getStorage } from 'firebase/storage';  // Import Firebase Storage
import { FirebaseApp, FirebaseOptions } from 'firebase/app';

// Your Firebase configuration
const firebaseConfig: FirebaseOptions = {
  apiKey: "AIzaSyCYm-2RgBY4N8833P3JLyB02qL4xLm6eTk",
  authDomain: "sijaisx.firebaseapp.com",
  projectId: "sijaisx",
  storageBucket: "sijaisx.firebasestorage.app",
  messagingSenderId: "557614086131",
  appId: "1:557614086131:web:817ca91eb8ee1c217b4486",
  measurementId: "G-0VXS30TXCN",
};

// Initialize Firebase app
const app: FirebaseApp = initializeApp(firebaseConfig);

// Initialize Firestore and Firebase Storage
const db = getFirestore(app);
const storage = getStorage(app);  // Firebase Storage initialized here

// Function to add a document (e.g., for teachers or substitutes) to Firestore
const addDataToFirestore = async (collectionName: string, data: any) => {
  try {
    const docRef = await addDoc(collection(db, collectionName), data);
    console.log("Document written with ID: ", docRef.id);
  } catch (e) {
    console.error("Error adding document: ", e);
  }
};

// Export Firestore and Firebase Storage for use in other parts of the app
export { db, storage, addDataToFirestore };
