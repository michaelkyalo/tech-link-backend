import { Navigate } from "react-router-dom";
import useAuth from "../features/auth/useAuth";

const RoleBasedRoute = ({ children, allowedRoles = [] }) => {
  const { user, loading } = useAuth();

  // ⏳ wait until auth is resolved
  if (loading) return null; // or spinner

  // 🔒 not logged in
  if (!user) {
    return <Navigate to="/login" replace />;
  }

  // 🚫 role not allowed
  if (!allowedRoles.includes(user.role)) {
    return <Navigate to="/" replace />;
  }

  return children;
};

export default RoleBasedRoute;