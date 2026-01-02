# Stuck Mind — Core Architecture (Uday Rawal)

Stuck Mind is not built to control me or fix me.  
It is built to stay with me when my mind feels stuck.

It is designed around four simple systems.

---

## 1. Listener

This is where everything starts.

- It accepts my raw thoughts, rants, and emotions.
- It does not judge what I say.
- It does not try to fix things immediately.
- It focuses on understanding before responding.

Sometimes being heard is enough.

---

## 2. Emotional Interpreter

This part helps Stuck Mind understand what I’m feeling.

- It reads my words to sense emotional states like:
  - stress
  - anxiety
  - tiredness
  - overwhelm
  - motivation
- It does not diagnose.
- It is not therapy.

Its job is only to understand my state, not to label me.

---

## 3. Memory System

Memory exists to build trust, not control.

- It remembers recurring problems.
- It notices emotional patterns over time.
- It remembers what helped me before and what didn’t.
- It never stores private thoughts marked as private.

Memory is used to support me, not to trap me in the past.

---

### Memory Flow (v1)

User input  
→ MemoryController  
→ MemoryInterface (rules)  
→ Journal / Memory  
→ Context  
→ Chat  

This flow enforces clear separation of responsibility:

- Chat handles interaction only  
- MemoryController routes data  
- MemoryInterface decides what is allowed  
- Journal and Memory store data  
- Context is returned without interpretation  

No emotion detection.  
No intelligence.  
Only safe, structured data flow.


## 4. Guide (Not a Boss)

This is how Stuck Mind helps me move forward.

- It suggests small, manageable next steps.
- It never orders me to act.
- It never pressures me with urgency.
- It speaks like a calm, mature version of me.

It guides when I’m ready, and stays when I’m not.

---

Stuck Mind is not here to make me productive.

It is here to make things feel lighter.
