function main() {
	let id = getInput();
	createKeyTable(id);
}
function createKeyTable(id) {
	console.log('id is '+id)
	id = convertToBase4(id);
	let val = validateId(id);
	if(!val[0])
	{
		alert("Your id was incorrect. Please try again");
		return;
	}
	let starting_color = val[1];
	renderTable(id, starting_color);
}
function getInput() {
	let id = document.getElementsByName("id")[0].value;
	return id;
}	
function renderTable(id, starting_color) {
	let table_code = "<table><tbody><tr>";
	let colors = ["Black", "Blue", "#FFFDD0", "Red"];
	for(let i = 0; i < id.length; i += 1)
	{
		table_code += "<td style='background-color:" + colors[id.charAt(i)] + ";'></td>";
		if(i % 5 == 4)
			table_code += "</tr><tr>";
	}
	table_code += "</tr><tr><td></td></tr><tr><td colspan='5' style='background-color:" + starting_color + ";'></td></tr></tbody></table>";
	document.getElementsByTagName("body")[0].innerHTML = table_code;
}
function convertToBase4(id) {
	return parseInt(id, 36).toString(4);
}
function validateId(id) {
	let countBlack = 0, countBlue = 0, countCream = 0, countRed = 0;
	if(id.length == 24)
		id = "0" + id;
	for(let i = 0; i < id.length; i += 1)
	{
		let chr = id.charAt(i);
		if(chr == '0')		countBlack += 1;
		else if(chr == '1')	countBlue += 1;
		else if(chr == '2')	countCream += 1;
		else			countRed += 1;
	}
	if(countBlack == 1 && countCream == 7 && countBlue == 9 && countRed == 8)
	{
		return [true, "Blue"];
	}
	else if(countBlack == 1 && countCream == 7 && countRed == 9 && countBlue == 8)
	{
		return [true, "Red"];
	}
	else
	{
		return [false, undefined];
	}
}