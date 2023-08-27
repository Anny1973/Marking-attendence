import React from 'react';

function StudentItem({ student, markAttendance }) {
  return (
    <li className="student-item">
      <span>{student.name}</span>
      <button
        onClick={() => markAttendance(student.id)}
        className={student.present ? 'present' : 'absent'}
      >
        {student.present ? 'Present' : 'Absent'}
      </button>
    </li>
  );
}

export default StudentItem;
