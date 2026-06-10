import {
  useEffect,
  useState
} from "react";

import {
  FaSave
} from "react-icons/fa";

import "../styles/settings.css";

function Settings() {

  const avatars = [

    "https://i.pravatar.cc/150?img=5",
    "https://i.pravatar.cc/150?img=9",
    "https://i.pravatar.cc/150?img=10",
    "https://i.pravatar.cc/150?img=12",
    "https://i.pravatar.cc/150?img=16",
    "https://i.pravatar.cc/150?img=20"

  ];

  const [showAvatars, setShowAvatars] =
    useState(false);

  const [savedMessage, setSavedMessage] =
    useState("");

  const [profileData, setProfileData] =
    useState({

      fullName: "Navya",

      email: "navya@gmail.com",

      phone: " ",

      role: "Event Planner",

      image:
        "https://i.pravatar.cc/150?img=12"
    });

  useEffect(() => {

   try {

  const savedSettings =
    localStorage.getItem(
      "eventSphereSettings"
    );

  if (savedSettings) {

    setProfileData(
      JSON.parse(savedSettings)
    );
  }

} catch (error) {

  console.error(
    "Failed to load settings",
    error
  );
}

  }, []);

const handleSave = () => {

  if (!profileData.fullName.trim()) {
    alert("Full Name is required");
    return;
  }

  if (!profileData.email.trim()) {
    alert("Email is required");
    return;
  }

  try {

  localStorage.setItem(
    "eventSphereSettings",
    JSON.stringify(profileData)
  );

} catch (error) {

  console.error(
    "Failed to save settings",
    error
  );
}

  setSavedMessage(
    "Changes Saved Successfully"
  );

  setTimeout(() => {
    setSavedMessage("");
  }, 2500);
};

  return (

    <div className="settings-page">

      <div className="settings-content">

        {/* TOP SECTION */}

        <div className="profile-top-section">

          {/* LEFT */}

          <div className="profile-left-side">

            <img
              src={profileData.image}
              alt="profile"
              className="profile-image"
            />

            <button
              className="change-photo-btn"

              onClick={() =>
                setShowAvatars(
                  !showAvatars
                )
              }
            >

              Change Photo

            </button>

            {

              showAvatars && (

                <div className="avatar-popup">

                  {

                    avatars.map(
                      (
                        avatar,
                        index
                      ) => (

                        <img
                          key={index}

                          src={avatar}

                          alt="avatar"

                          className="avatar-option"

                          onClick={() => {

                            setProfileData({

                              ...profileData,

                              image: avatar
                            });

                            setShowAvatars(
                              false
                            );
                          }}
                        />
                      )
                    )
                  }

                </div>
              )
            }

          </div>

          {/* RIGHT */}

          <div className="profile-meta">

            <h1 className="profile-name">

              {profileData.fullName}

            </h1>

            <p className="profile-description">

              Manage your personal account preferences and AI workspace settings.

            </p>

            <div className="profile-badge">

              AI Event Planner Pro

            </div>

          </div>

        </div>

        {/* FORM */}

        <div className="settings-form">

          <div className="form-group">

            <label>
              Full Name
            </label>

            <input
              type="text"

              value={
                profileData.fullName
              }

              onChange={(e) =>
                setProfileData({

                  ...profileData,

                  fullName:
                    e.target.value
                })
              }
            />

          </div>

          <div className="form-group">

            <label>
              Email
            </label>

            <input
              type="email"

              value={
                profileData.email
              }

              onChange={(e) =>
                setProfileData({

                  ...profileData,

                  email:
                    e.target.value
                })
              }
            />

          </div>

          <div className="form-group">

            <label>
              Phone
            </label>

            <input
              type="text"

              value={
                profileData.phone
              }

              onChange={(e) =>
                setProfileData({

                  ...profileData,

                  phone:
                    e.target.value
                })
              }
            />

          </div>

          <div className="form-group">

            <label>
              Role
            </label>

            <input
              type="text"

              value={profileData.role}
              readOnly

            />

          </div>

        </div>

        {/* SAVE */}

        <div className="bottom-save-btn">

          {

            savedMessage && (

              <span className="saved-text">

                {savedMessage}

              </span>
            )
          }

          <button
            className="save-btn"
            onClick={handleSave}
          >

            <FaSave />

            Save Changes

          </button>

        </div>

      </div>

    </div>
  );
}

export default Settings;