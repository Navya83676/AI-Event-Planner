import {
  useState,
  useContext,
  useMemo,
  useEffect
} from "react";

import {
  Search,
  Store,
  Star,
  CheckCircle,
  Clock,
  Trash2,
  Pencil,
  X
} from "lucide-react";

import "../styles/vendors.css";

import {
  EventContext
} from "../context/EventContext";

import StatCard from "../components/StatCard";

/* =========================
   AI FALLBACK VENDORS
========================= */



function Vendors() {

  const {
    eventData,
    setEventData
  } = useContext(EventContext);

  const [search, setSearch] =
    useState("");

  const [showModal, setShowModal] =
    useState(false);

  const [editingId, setEditingId] =
    useState(null);

  const [vendors, setVendors] =
    useState([]);

  const [newVendor, setNewVendor] =
    useState({

      name: "",

      category: "",

      rating: 4.5,

      status: "Confirmed"
    });

    /* =========================
   LOAD VENDORS
========================= */

useEffect(() => {

  console.log(
    "EVENT DATA VENDORS:",
    eventData?.vendors
  );

  setVendors(

    Array.isArray(
      eventData?.vendors
    )

      ? eventData.vendors

      : []

  );

}, [eventData]);
  /* =========================
     FILTER
  ========================= */

  const filteredVendors =
    useMemo(() => {

      return vendors.filter(
        (vendor) =>

          [

            vendor.name,
            vendor.category,
            vendor.status

          ]

            .join(" ")

            .toLowerCase()

            .includes(
              search.toLowerCase()
            )
      );

    }, [
      vendors,
      search
    ]);

  /* =========================
     STATS
  ========================= */

  const confirmedVendors =
    vendors.filter(
      (v) =>
        v.status === "Confirmed"
    ).length;

  const pendingVendors =
    vendors.filter(
      (v) =>
        v.status === "Pending"
    ).length;

  const averageRating =

    vendors.length > 0

      ? (
          vendors.reduce(
            (acc, vendor) =>

              acc + Number(vendor.rating || 0),

            0
          ) / vendors.length
        ).toFixed(1)

      : "0.0";

  /* =========================
     ADD / UPDATE
  ========================= */

  const handleSaveVendor = () => {

    if (

      !newVendor.name ||

      !newVendor.category

    ) return;

    let updatedVendors = [];

    if (editingId) {

      updatedVendors = vendors.map(
        (vendor) =>

          vendor.id === editingId

            ? {

                ...newVendor,

                id: editingId
              }

            : vendor
      );

    } else {

      updatedVendors = [

        ...vendors,

        {

          ...newVendor,

          id:
            crypto.randomUUID()
        }
      ];
    }

    setVendors(updatedVendors);

    setEventData({

      ...eventData,

      vendors: updatedVendors
    });

    setNewVendor({

      name: "",

      category: "",

      rating: 4.5,

      status: "Confirmed"
    });

    setEditingId(null);

    setShowModal(false);
  };

  /* =========================
     DELETE
  ========================= */

  const handleDeleteVendor = (
    vendorId
  ) => {

    const updated =
      vendors.filter(
        (vendor) =>
          vendor.id !== vendorId
      );

    setVendors(updated);

    setEventData({

      ...eventData,

      vendors: updated
    });
  };

  /* =========================
     EDIT
  ========================= */

  const handleEditVendor = (
    vendor
  ) => {

    setNewVendor(vendor);

    setEditingId(vendor.id);

    setShowModal(true);
  };

  return (

    <div className="page-content">

      {/* HEADER */}

      <div className="page-header">

        <div>

          <h1 className="page-title">
            Vendors ({vendors.length})
          </h1>

          <p className="page-subtitle">

            AI powered vendor
            orchestration platform

          </p>

        </div>

        <button
          className="primary-btn"
          onClick={() => {

            setShowModal(true);

            setEditingId(null);

            setNewVendor({

              name: "",

              category: "",

              rating: 4.5,

              status: "Confirmed"
            });
          }}
        >

          + Add Vendor

        </button>

      </div>

      {/* STATS */}

      <div className="grid-4 section-spacing">

        <StatCard
          icon={<Store />}
          title="Total Vendors"
          value={vendors.length}
          subtitle="AI managed partners"
          color="purple"
        />

        <StatCard
          icon={<CheckCircle />}
          title="Confirmed"
          value={confirmedVendors}
          subtitle="Ready for execution"
          color="green"
        />

        <StatCard
          icon={<Clock />}
          title="Pending"
          value={pendingVendors}
          subtitle="Pending confirmation"
          color="orange"
        />

        <StatCard
          icon={<Star />}
          title="Average Rating"
          value={averageRating}
          subtitle="Average service quality"
          color="blue"
        />

      </div>

      {/* TABLE */}

      <div className="global-card section-spacing">

        <div className="vendors-table-top">

          <div className="vendors-search-box">

            <Search size={18} />

            <input
              type="text"
              placeholder="Search vendors..."
              value={search}
              onChange={(e) =>
                setSearch(
                  e.target.value
                )
              }
            />

          </div>

        </div>

        <div className="table-container">

          <table className="global-table">

            <thead>

              <tr>

                <th>
                  Vendor Name
                </th>

                <th>
                  Category
                </th>

                <th>
                  Rating
                </th>

                <th>
                  Status
                </th>

                <th>
                  Actions
                </th>

              </tr>

            </thead>

            <tbody>

              {

                filteredVendors.length > 0

                  ? filteredVendors.map(
                      (
                        vendor
                      ) => (

                        <tr key={vendor.id}>

                          <td>
                            {vendor.name}
                          </td>

                          <td>
                            {vendor.category}
                          </td>

                          <td>

                            <div className="vendor-rating">

                              <Star
                                size={14}
                                fill="currentColor"
                              />

                              <span>
                                {vendor.rating}
                              </span>

                            </div>

                          </td>

                          <td>

                            <span
                              className={`status-badge ${
                                vendor.status ===
                                "Confirmed"

                                  ? "status-success"

                                  : "status-warning"
                              }`}
                            >

                              {vendor.status}

                            </span>

                          </td>

                          <td>

                            <div
                              style={{
                                display: "flex",
                                gap: "10px"
                              }}
                            >

                              <button
                                className="vendors-action-btn"
                                onClick={() =>
                                  handleEditVendor(
                                    vendor
                                  )
                                }
                              >

                                <Pencil size={16} />

                              </button>

                              <button
                                className="vendors-action-btn"
                                onClick={() =>
                                  handleDeleteVendor(
                                    vendor.id
                                  )
                                }
                              >

                                <Trash2 size={16} />

                              </button>

                            </div>

                          </td>

                        </tr>
                      )
                    )

                  : (

                    <tr>

                      <td
                        colSpan="5"
                        className="text-center"
                      >

                        No vendors found.

                      </td>

                    </tr>
                  )
              }

            </tbody>

          </table>

        </div>

      </div>

      {/* MODAL */}

      {

        showModal && (

          <div className="vendor-modal-overlay">

            <div className="vendor-modal">

              <div
                style={{
                  display: "flex",
                  justifyContent: "space-between",
                  alignItems: "center"
                }}
              >

                <h2>

                  {

                    editingId

                      ? "Edit Vendor"

                      : "Add Vendor"
                  }

                </h2>

                <button
                  className="vendors-action-btn"
                  onClick={() =>
                    setShowModal(false)
                  }
                >

                  <X size={18} />

                </button>

              </div>

              <input
                type="text"
                placeholder="Vendor Name"
                value={newVendor.name}
                onChange={(e) =>
                  setNewVendor({

                    ...newVendor,

                    name: e.target.value
                  })
                }
              />

              <input
                type="text"
                placeholder="Category"
                value={newVendor.category}
                onChange={(e) =>
                  setNewVendor({

                    ...newVendor,

                    category: e.target.value
                  })
                }
              />

              <input
                type="number"
                step="0.1"
                min="1"
                max="5"
                placeholder="Rating"
                value={newVendor.rating}
                onChange={(e) =>
                  setNewVendor({

                    ...newVendor,

                    rating: e.target.value
                  })
                }
              />

              <select
                value={newVendor.status}
                onChange={(e) =>
                  setNewVendor({

                    ...newVendor,

                    status: e.target.value
                  })
                }
              >

                <option>
                  Confirmed
                </option>

                <option>
                  Pending
                </option>

              </select>

              <div className="vendor-modal-buttons">

                <button
                  className="secondary-btn"
                  onClick={() =>
                    setShowModal(false)
                  }
                >

                  Cancel

                </button>

                <button
                  className="primary-btn"
                  onClick={
                    handleSaveVendor
                  }
                >

                  {

                    editingId

                      ? "Update Vendor"

                      : "Add Vendor"
                  }

                </button>

              </div>

            </div>

          </div>
        )
      }

    </div>
  );
}

export default Vendors;