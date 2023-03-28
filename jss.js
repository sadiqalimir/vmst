function calculateTorsion() {
    const length = document.getElementById("length").value;
    const diameter = document.getElementById("diameter").value;
    const angle = document.getElementById("angle").value;
  
    const radius = diameter / 2;
    const torsionConstant = (Math.PI * Math.pow(radius, 4)) / 2;
  
    const torsion = (torsionConstant * length * angle) / (180 * Math.PI);
  
    document.getElementById("result").innerHTML = `Torsion: ${torsion.toFixed(2)} Nm`;
  }