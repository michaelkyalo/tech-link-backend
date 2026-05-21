import { Link } from "react-router-dom";

const stats = [
  { label: "Total Orders", value: 12, color: "#16a34a", bg: "#dcfce7" },
  { label: "Cart Items", value: 5, color: "#2563eb", bg: "#dbeafe" },
  { label: "Delivered Orders", value: 9, color: "#d97706", bg: "#fef3c7" },
];

const actions = [
  { label: "🛒 Browse Products", to: "/products", color: "#16a34a" },
  { label: "🛍️ View Cart", to: "/cart", color: "#2563eb" },
  { label: "📦 My Orders", to: "/orders", color: "#d97706" },
  { label: "💬 Open Chat", to: "/chat", color: "#7c3aed" },
];

const activity = [
  { icon: "🛒", text: "Added Tomatoes to cart", time: "2m ago", tag: "Cart", tagBg: "#dcfce7", tagColor: "#16a34a" },
  { icon: "📦", text: "Order #102 delivered", time: "1h ago", tag: "Order", tagBg: "#dbeafe", tagColor: "#2563eb" },
  { icon: "💬", text: "Sent message to farmer", time: "3h ago", tag: "Chat", tagBg: "#ede9fe", tagColor: "#7c3aed" },
  { icon: "💳", text: "Payment completed successfully", time: "Yesterday", tag: "Payment", tagBg: "#fef3c7", tagColor: "#d97706" },
];

const BuyerDashboard = () => (
  <div style={{ backgroundColor: "#f0f4f8", minHeight: "100vh", padding: "16px", fontFamily: "sans-serif" }}>

    {/* Header */}
    <div style={{ background: "linear-gradient(135deg, #14532d, #16a34a)", borderRadius: "16px", padding: "22px 24px", color: "white", display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: "16px" }}>
      <div>
        <h1 style={{ margin: 0, fontSize: "22px", fontWeight: 700 }}>🌿 Buyer Dashboard</h1>
        <p style={{ margin: "4px 0 0", color: "#bbf7d0", fontSize: "13px" }}>Welcome back! Explore fresh farm products.</p>
      </div>
      <Link to="/products" style={{ background: "white", color: "#16a34a", fontWeight: 600, padding: "8px 16px", borderRadius: "8px", textDecoration: "none", fontSize: "14px" }}>
        + Browse
      </Link>
    </div>

    {/* Stats */}
    <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr 1fr", gap: "12px", marginBottom: "16px" }}>
      {stats.map((s) => (
        <div key={s.label} style={{ background: "white", borderRadius: "14px", padding: "16px", boxShadow: "0 1px 6px rgba(0,0,0,0.06)" }}>
          <div style={{ background: s.bg, borderRadius: "8px", width: "36px", height: "36px", display: "flex", alignItems: "center", justifyContent: "center", marginBottom: "10px", fontSize: "18px" }}>
            {s.label === "Total Orders" ? "📋" : s.label === "Cart Items" ? "🛍️" : "✅"}
          </div>
          <p style={{ margin: 0, fontSize: "12px", color: "#6b7280" }}>{s.label}</p>
          <p style={{ margin: "4px 0 0", fontSize: "28px", fontWeight: 700, color: s.color }}>{s.value}</p>
        </div>
      ))}
    </div>

    {/* Quick Actions */}
    <div style={{ background: "white", borderRadius: "14px", padding: "18px", boxShadow: "0 1px 6px rgba(0,0,0,0.06)", marginBottom: "16px" }}>
      <h2 style={{ margin: "0 0 14px", fontSize: "16px", fontWeight: 700 }}>Quick Actions</h2>
      <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "10px" }}>
        {actions.map((a) => (
          <Link key={a.to} to={a.to} style={{ background: a.color, color: "white", textDecoration: "none", padding: "14px", borderRadius: "12px", fontWeight: 600, fontSize: "14px", textAlign: "center", display: "block" }}>
            {a.label}
          </Link>
        ))}
      </div>
    </div>

    {/* Recent Activity */}
    <div style={{ background: "white", borderRadius: "14px", padding: "18px", boxShadow: "0 1px 6px rgba(0,0,0,0.06)" }}>
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: "12px" }}>
        <h2 style={{ margin: 0, fontSize: "16px", fontWeight: 700 }}>Recent Activity</h2>
        <Link to="/activity" style={{ color: "#16a34a", fontSize: "13px", fontWeight: 600, textDecoration: "none" }}>See all</Link>
      </div>
      {activity.map((item, i) => (
        <div key={i} style={{ display: "flex", justifyContent: "space-between", alignItems: "center", padding: "12px 0", borderBottom: i < activity.length - 1 ? "1px solid #f3f4f6" : "none" }}>
          <span style={{ fontSize: "14px" }}>{item.icon} {item.text}</span>
          <div style={{ textAlign: "right", flexShrink: 0, marginLeft: "12px" }}>
            <div style={{ fontSize: "11px", color: "#9ca3af" }}>{item.time}</div>
            <span style={{ fontSize: "11px", background: item.tagBg, color: item.tagColor, borderRadius: "6px", padding: "2px 8px", fontWeight: 600 }}>{item.tag}</span>
          </div>
        </div>
      ))}
    </div>

  </div>
);

export default BuyerDashboard;