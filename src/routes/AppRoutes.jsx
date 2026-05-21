import { BrowserRouter, Routes, Route } from "react-router-dom";

// Layout
import MainLayout from "../layouts/MainLayout";

// Pages
import Home from "../Home";

// Auth
import Login from "../features/auth/Login";
import Register from "../features/auth/Register";

// Buyer
import BuyerDashboard from "../features/buyer/BuyerDashboard";
import Products from "../features/buyer/Products";
import ProductDetails from "../features/buyer/ProductsDetails";
import Cart from "../features/buyer/Cart";
import Checkout from "../features/buyer/Checkout";
import Orders from "../features/buyer/Orders";

// Farmer
import FarmerDashboard from "../features/farmer/FarmerDashboard";
import AddProduct from "../features/farmer/AddProduct";
import FarmProduct from "../features/farmer/FarmProduct";
import FarmerOrders from "../features/farmer/FarmerOrders";

// Admin
import AdminDashboard from "../features/admin/AdminDashboard";

// Chat
import ChatPage from "../features/chat/chatPage";

// Guards
import ProtectedRoute from "./ProtectedRoute";
import RoleBasedRoute from "./RoleBasedRoute";

export default function AppRoutes() {
  return (
    <BrowserRouter>
      <Routes>

        {/* ================= PUBLIC ================= */}
        <Route element={<MainLayout />}>
          <Route path="/" element={<Home />} />
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />

          {/* ================= CHAT ================= */}
          <Route
            path="/chat"
            element={
              <ProtectedRoute>
                <ChatPage />
              </ProtectedRoute>
            }
          />

          {/* ================= BUYER ================= */}
          <Route
            path="/buyer"
            element={
              <ProtectedRoute>
                <RoleBasedRoute allowedRoles={["buyer"]}>
                  <BuyerDashboard />
                </RoleBasedRoute>
              </ProtectedRoute>
            }
          />

          <Route
            path="/buyer/products"
            element={<ProtectedRoute><Products /></ProtectedRoute>}
          />

          <Route
            path="/buyer/products/:id"
            element={<ProtectedRoute><ProductDetails /></ProtectedRoute>}
          />

          <Route
            path="/buyer/cart"
            element={<ProtectedRoute><Cart /></ProtectedRoute>}
          />

          <Route
            path="/buyer/checkout"
            element={<ProtectedRoute><Checkout /></ProtectedRoute>}
          />

          <Route
            path="/buyer/orders"
            element={<ProtectedRoute><Orders /></ProtectedRoute>}
          />

          {/* ================= FARMER ================= */}
          <Route
            path="/farmer"
            element={
              <ProtectedRoute>
                <RoleBasedRoute allowedRoles={["farmer"]}>
                  <FarmerDashboard />
                </RoleBasedRoute>
              </ProtectedRoute>
            }
          />

          <Route
            path="/farmer/add-product"
            element={<ProtectedRoute><AddProduct /></ProtectedRoute>}
          />

          <Route
            path="/farmer/products"
            element={
              <ProtectedRoute>
                <RoleBasedRoute allowedRoles={["farmer"]}>
                  <FarmProduct />
                </RoleBasedRoute>
              </ProtectedRoute>
            }
          />

          <Route
            path="/farmer/orders"
            element={<ProtectedRoute><FarmerOrders /></ProtectedRoute>}
          />

          {/* ================= ADMIN ================= */}
          <Route
            path="/admin"
            element={
              <ProtectedRoute>
                <RoleBasedRoute allowedRoles={["admin"]}>
                  <AdminDashboard />
                </RoleBasedRoute>
              </ProtectedRoute>
            }
          />

          {/* ================= 404 ================= */}
          <Route
            path="*"
            element={
              <div style={{ textAlign: "center", padding: "40px" }}>
                <h1>404 - Page Not Found</h1>
                <p>The page you are looking for does not exist.</p>
              </div>
            }
          />
        </Route>

      </Routes>
    </BrowserRouter>
  );
}