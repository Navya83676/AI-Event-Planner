export const safeValue = (
  value,
  fallback = "N/A"
) => {

  if (
    value === null ||
    value === undefined ||
    value === ""
  ) {

    return fallback;
  }

  return value;
};

export const safeNumber = (
  value,
  fallback = 0
) => {

  const number =
    Number(value);

  return isNaN(number)
    ? fallback
    : number;
};

export const safeCurrency = (
  value
) => {

  return safeNumber(value)
    .toLocaleString();
};

export const safeArray = (
  value
) => {

  return Array.isArray(value)
    ? value
    : [];
};

export const safeObject = (
  value
) => {

  return (
    typeof value === "object" &&
    value !== null
  )

    ? value

    : {};
};

export const formatAgent = (
  agent
) => {

  if (!agent) {
    return "Unknown Agent";
  }

  if (
    typeof agent === "string"
  ) {

    return agent;
  }

  if (
    typeof agent === "object"
  ) {

    return (

      agent?.name ||

      agent?.agent ||

      agent?.title ||

      JSON.stringify(agent)
    );
  }

  return String(agent);
};