import { Link } from "react-router-dom";

export default function FarmerDashboard() {
  const stats = [
    { label: "Total products", value: "24", badge: "+3", color: "#3a6b1e" },
    { label: "Orders received", value: "18", badge: "+5", color: "#2563eb" },
    { label: "Revenue", value: "KES 45,000", badge: "↑12%", color: "#b45309" },
  ];

  const actions = [
    { title: "Add new product", sub: "List crops for sale", link: "/add-product" },
    { title: "View products", sub: "Manage your listings", link: "/products" },
    { title: "View orders", sub: "Track buyer requests", link: "/orders" },
    { title: "Open chat", sub: "Message buyers", link: "/chat" },
  ];

  const activity = [
    { text: "New order received for Maize", time: "2m ago", tag: "Order" },
    { text: "Product Carrots added successfully", time: "1h ago", tag: "Product" },
    { text: "New message from buyer", time: "3h ago", tag: "Chat" },
    { text: "Delivery marked as completed", time: "Yesterday", tag: "Delivery" },
  ];

  return (
    <div style={{ backgroundColor: "#f0f2ed", minHeight: "100vh", padding: "16px", fontFamily: "sans-serif" }}>

      {/* Header */}
      <div style={{ background: "#2d5016", borderRadius: "16px", padding: "20px", color: "white", display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: "16px" }}>
        <div>
          <h2 style={{ margin: 0 }}>🌱 Farmer Dashboard</h2>
          <p style={{ margin: 0, color: "#a8c97f", fontSize: "14px" }}>Welcome back! Thursday, 21 May 2026</p>
        </div>
        <button style={{ background: "rgba(255,255,255,0.15)", border: "1px solid white", color: "white", padding: "8px 16px", borderRadius: "8px", cursor: "pointer" }}>
          + Add product
        </button>
      </div>

      {/* Stats */}
      <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr 1fr", gap: "12px", marginBottom: "16px" }}>
        {stats.map((s) => (
          <div key={s.label} style={{ background: "white", borderRadius: "12px", padding: "16px" }}>
            <div style={{ display: "flex", justifyContent: "space-between" }}>
              <span style={{ fontSize: "13px", color: "#666" }}>{s.label}</span>
              <span style={{ fontSize: "12px", color: s.color, fontWeight: "bold" }}>{s.badge}</span>
            </div>
            <p style={{ margin: "8px 0 0", fontWeight: "bold", fontSize: "22px", color: s.color }}>{s.value}</p>
          </div>
        ))}
      </div>

      {/* Quick Actions */}
      <div style={{ background: "white", borderRadius: "12px", padding: "16px", marginBottom: "16px" }}>
        <h3 style={{ margin: "0 0 12px" }}>Quick actions</h3>
        <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "10px" }}>
          {actions.map((a) => (
            <Link key={a.title} to={a.link} style={{ background: "#f9fafb", border: "1px solid #eee", borderRadius: "10px", padding: "12px", textDecoration: "none", display: "block" }}>
              <div style={{ fontWeight: "bold", fontSize: "14px", color: "#111" }}>{a.title}</div>
              <div style={{ fontSize: "12px", color: "#999" }}>{a.sub}</div>
            </Link>
          ))}
        </div>
      </div>

      {/* Recent Activity */}
      <div style={{ background: "white", borderRadius: "12px", padding: "16px" }}>
        <div style={{ display: "flex", justifyContent: "space-between", marginBottom: "12px" }}>
          <h3 style={{ margin: 0 }}>Recent activity</h3>
          <span style={{ color: "#3a6b1e", cursor: "pointer", fontSize: "14px" }}>See all</span>
        </div>
        {activity.map((item, i) => (
          <div key={i} style={{ display: "flex", justifyContent: "space-between", padding: "12px 0", borderBottom: i < activity.length - 1 ? "1px solid #f3f4f6" : "none" }}>
            <span style={{ fontSize: "14px" }}>● {item.text}</span>
            <div style={{ textAlign: "right" }}>
              <div style={{ fontSize: "12px", color: "#999" }}>{item.time}</div>
              <span style={{ fontSize: "12px", background: "#f3f4f6", borderRadius: "6px", padding: "2px 8px" }}>{item.tag}</span>
            </div>
          </div>
        ))}
      </div>

    </div>
  );
}