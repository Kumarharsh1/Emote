export const createPageUrl = (pageName) => {
  return `/${pageName.toLowerCase()}`
}

export const emotionColors = {
  happy: { bg: "from-green-500 to-emerald-500", text: "text-green-400", color: "#22c55e" },
  sad: { bg: "from-blue-500 to-indigo-500", text: "text-blue-400", color: "#3b82f6" },
  angry: { bg: "from-red-500 to-rose-500", text: "text-red-400", color: "#ef4444" },
  surprised: { bg: "from-yellow-500 to-orange-500", text: "text-yellow-400", color: "#f59e0b" },
  neutral: { bg: "from-gray-500 to-slate-500", text: "text-gray-400", color: "#6b7280" },
  fearful: { bg: "from-purple-500 to-violet-500", text: "text-purple-400", color: "#8b5cf6" },
  disgusted: { bg: "from-pink-500 to-fuchsia-500", text: "text-pink-400", color: "#ec4899" },
  excited: { bg: "from-lime-500 to-green-500", text: "text-lime-400", color: "#10b981" },
  confused: { bg: "from-orange-500 to-red-500", text: "text-orange-400", color: "#f97316" },
  bored: { bg: "from-slate-500 to-gray-500", text: "text-slate-400", color: "#64748b" },
  anxious: { bg: "from-violet-500 to-purple-500", text: "text-violet-400", color: "#a855f7" },
  content: { bg: "from-teal-500 to-cyan-500", text: "text-teal-400", color: "#14b8a6" }
}